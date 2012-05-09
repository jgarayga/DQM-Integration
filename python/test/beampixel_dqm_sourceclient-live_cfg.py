import FWCore.ParameterSet.Config as cms

process = cms.Process("BeamPixel")


#----------------------------
# Common for PP and HI running
#----------------------------
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("DQM.Integration.test.inputsource_cfi")
process.DQMEventStreamHttpReader.consumerName = "Beam Pixel DQM Consumer"


#----------------------------
# HLT Filter
#----------------------------
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1
process.physicsBitSelector = cms.EDFilter("PhysDecl",
                                          applyfilter = cms.untracked.bool(True),
                                          debugOn     = cms.untracked.bool(False))
# L1 Filter
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff")
process.load("HLTrigger.HLTfilters.hltLevel1GTSeed_cfi")
process.hltLevel1GTSeed.L1TechTriggerSeeding = cms.bool(True)
process.hltLevel1GTSeed.L1SeedsLogicalExpression = cms.string("0 AND (40 OR 41) AND NOT (36 OR 37 OR 38 OR 39) AND (NOT 42 OR 43) AND (42 OR NOT 43)")


#----------------------------
# DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
### @@@@@@ Un-comment when running locally @@@@@@ ###
#process.DQM.collectorHost = ''
### @@@@@@ Un-comment when running locally @@@@@@ ###
process.dqmEnv.subSystemFolder = "BeamPixel"


#----------------------------
# Sub-system Configuration
#----------------------------
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("RecoTracker.TkTrackingRegions.GlobalTrackingRegion_cfi")
process.load("RecoVertex.PrimaryVertexProducer.OfflinePixel3DPrimaryVertices_cfi")


#----------------------------
# Define Sequence
#----------------------------
process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)
process.phystrigger = cms.Sequence(process.hltTriggerTypeFilter
                                    ### To use the L1 Filter uncomment the following line ###
                                    #  *process.gtDigis*process.hltLevel1GTSeed
                                   )




#--------------------------------------------------
# Proton-Proton Specific Part
#--------------------------------------------------
if (process.runType.getRunType() == process.runType.pp_run or process.runType.getRunType() == process.runType.cosmic_run):
    print "Running pp "

    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_L1*',
                                                                                                  'HLT_Jet*',
                                                                                                  'HLT_*Cosmic*',
                                                                                                  'HLT_HT*',
                                                                                                  'HLT_MinBias_*',
                                                                                                  'HLT_Physics*',
                                                                                                  'HLT_ZeroBias*'))

    process.load("Configuration.StandardSequences.Reconstruction_cff")


    #----------------------------
    # pixelVertexDQM Configuration
    #----------------------------
    process.pixelVertexDQM = cms.EDAnalyzer("Vx3DHLTAnalyzer",
                                            vertexCollection = cms.InputTag("pixelVertices"),
                                            debugMode        = cms.bool(True),
                                            nLumiReset       = cms.uint32(2),
                                            dataFromFit      = cms.bool(True),
                                            minNentries      = cms.uint32(20),
                                            # If the histogram has at least "minNentries" then extract Mean and RMS,
                                            # or, if we are performing the fit, the number of vertices must be greater
                                            # than minNentries otherwise it waits for other nLumiReset
                                            xRange           = cms.double(2.0),
                                            xStep            = cms.double(0.001),
                                            yRange           = cms.double(2.0),
                                            yStep            = cms.double(0.001),
                                            zRange           = cms.double(30.0),
                                            zStep            = cms.double(0.05),
                                            VxErrCorr        = cms.double(1.37),  # Keep checking this with later release
                                            fileName         = cms.string("/nfshome0/yumiceva/BeamMonitorDQM/BeamPixelResults.txt"))
    if process.dqmSaver.producer.value() is "Playback":
       process.pixelVertexDQM.fileName = cms.string("/nfshome0/dqmdev/BeamMonitorDQM/BeamPixelResults.txt")
    else:
       process.pixelVertexDQM.fileName = cms.string("/nfshome0/dqmpro/BeamMonitorDQM/BeamPixelResults.txt")


    #----------------------------
    # Pixel-Tracks Configuration
    #----------------------------
    process.pixelVertices.TkFilterParameters.minPt = process.pixelTracks.RegionFactoryPSet.RegionPSet.ptMin


    #----------------------------
    # Pixel-Vertices Configuration
    #----------------------------
    process.reconstruction_step = cms.Sequence(process.siPixelDigis*
                                               process.offlineBeamSpot*
                                               process.siPixelClusters*
                                               process.siPixelRecHits*
                                               process.pixelTracks*
                                               process.pixelVertices*
                                               process.pixelVertexDQM)

    #----------------------------
    # Define Path
    #----------------------------
    process.p = cms.Path(process.phystrigger*
                         process.reconstruction_step*
                         process.dqmmodules)


process.castorDigis.InputLabel = cms.InputTag("rawDataCollector")
process.csctfDigis.producer = cms.InputTag("rawDataCollector")
process.dttfDigis.DTTF_FED_Source = cms.InputTag("rawDataCollector")
process.ecalDigis.InputLabel = cms.InputTag("rawDataCollector")
process.ecalPreshowerDigis.sourceTag = cms.InputTag("rawDataCollector")
process.gctDigis.inputLabel = cms.InputTag("rawDataCollector")
process.gtDigis.DaqGtInputTag = cms.InputTag("rawDataCollector")
process.gtEvmDigis.EvmGtInputTag = cms.InputTag("rawDataCollector")
process.hcalDigis.InputLabel = cms.InputTag("rawDataCollector")
process.muonCSCDigis.InputObjects = cms.InputTag("rawDataCollector")
process.muonDTDigis.inputLabel = cms.InputTag("rawDataCollector")
process.muonRPCDigis.InputLabel = cms.InputTag("rawDataCollector")
process.scalersRawToDigi.scalersInputTag = cms.InputTag("rawDataCollector")
process.siPixelDigis.InputLabel = cms.InputTag("rawDataCollector")
process.siStripDigis.ProductLabel = cms.InputTag("rawDataCollector")




#--------------------------------------------------
# Heavy Ion Specific Part
#--------------------------------------------------
if (process.runType.getRunType() == process.runType.hi_run):
    print "Running HI "
    
    process.castorDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.csctfDigis.producer = cms.InputTag("rawDataRepacker")
    process.dttfDigis.DTTF_FED_Source = cms.InputTag("rawDataRepacker")
    process.ecalDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.ecalPreshowerDigis.sourceTag = cms.InputTag("rawDataRepacker")
    process.gctDigis.inputLabel = cms.InputTag("rawDataRepacker")
    process.gtDigis.DaqGtInputTag = cms.InputTag("rawDataRepacker")
    process.gtEvmDigis.EvmGtInputTag = cms.InputTag("rawDataRepacker")
    process.hcalDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.muonCSCDigis.InputObjects = cms.InputTag("rawDataRepacker")
    process.muonDTDigis.inputLabel = cms.InputTag("rawDataRepacker")
    process.muonRPCDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.scalersRawToDigi.scalersInputTag = cms.InputTag("rawDataRepacker")
    process.siPixelDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.siStripDigis.ProductLabel = cms.InputTag("rawDataRepacker")

    process.load("Configuration.StandardSequences.ReconstructionHeavyIons_cff") # HI sequences

    process.DQMEventStreamHttpReader.consumerName = "Beam Pixel DQM Consumer"
    process.DQMEventStreamHttpReader.SelectEvents =  cms.untracked.PSet(SelectEvents = cms.vstring( 'HLT_HI*'))


    #----------------------------
    # pixelVertexDQM Configuration
    #----------------------------
    process.pixelVertexDQM = cms.EDAnalyzer("Vx3DHLTAnalyzer",
                                            vertexCollection = cms.InputTag("hiSelectedVertex"),
                                            debugMode        = cms.bool(True),
                                            nLumiReset       = cms.uint32(5),
                                            dataFromFit      = cms.bool(True),
                                            minNentries      = cms.uint32(20),
                                            # If the histogram has at least "minNentries" then extract Mean and RMS,
                                            # or, if we are performing the fit, the number of vertices must be greater
                                            # than minNentries otherwise it waits for other nLumiReset
                                            xRange           = cms.double(2.0),
                                            xStep            = cms.double(0.001),
                                            yRange           = cms.double(2.0),
                                            yStep            = cms.double(0.001),
                                            zRange           = cms.double(30.0),
                                            zStep            = cms.double(0.05),
                                            VxErrCorr        = cms.double(1.37),
                                            fileName         = cms.string("/nfshome0/yumiceva/BeamMonitorDQM/BeamPixelResults.txt"))
    if process.dqmSaver.producer.value() is "Playback":
       process.pixelVertexDQM.fileName = cms.string("/nfshome0/dqmdev/BeamMonitorDQM/BeamPixelResults.txt")
    else:
       process.pixelVertexDQM.fileName = cms.string("/nfshome0/dqmpro/BeamMonitorDQM/BeamPixelResults.txt")


    #----------------------------
    # Pixel-Tracks Configuration
    #----------------------------
    #process.PixelTrackReconstructionBlock.RegionFactoryPSet.ComponentName = "GlobalRegionProducer"


    #----------------------------
    # Pixel-Vertices Configuration
    #----------------------------
    process.reconstruction_step = cms.Sequence(process.siPixelDigis*
                                               process.offlineBeamSpot*
                                               process.siPixelClusters*
                                               process.siPixelRecHits*
                                               process.offlineBeamSpot*
                                               process.hiPixelVertices*
                                               process.pixelVertexDQM)


    #----------------------------
    # Define Path
    #----------------------------
    process.p = cms.Path(process.phystrigger*
                         process.reconstruction_step*
                         process.dqmmodules)
