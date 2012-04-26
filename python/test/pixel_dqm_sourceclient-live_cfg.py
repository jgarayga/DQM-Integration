import FWCore.ParameterSet.Config as cms

process = cms.Process("PIXELDQMLIVE")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelDigis', 
                                         #'siPixelClusters', 
                                         'SiPixelRawDataErrorSource', 
                                         'SiPixelDigiSource', 
                                         #'SiPixelClusterSource',
					 'sipixelEDAClient'),
    cout = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
    destinations = cms.untracked.vstring('cout')
)

QTestfile = 'DQM/SiPixelMonitorClient/test/sipixel_qualitytest_config.xml'
#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.DQMEventStreamHttpReader.consumerName = 'Pixel DQM Consumer'
process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('HLT_L1*','HLT_Jet*','HLT_*Cosmic*','HLT_HT*','HLT_MinBias_*','HLT_Physics*', 'HLT_ZeroBias*'))

#process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_Rando*'))
#process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('*'))
#process.DQMEventStreamHttpReader.sourceURL = cms.string('http://srv-c2c05-07.cms:22100/urn:xdaq-application:lid=30')
##
#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder    = "Pixel"
process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/pixel_reference_pp.root'
if (process.runType.getRunType() == process.runType.hi_run):
    process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/pixel_reference_hi.root'

if (process.runType.getRunType() == process.runType.cosmic_run):
    process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/pixel_reference_cosmic.root'

#-----------------------------
# Magnetic Field
#-----------------------------
# 0T field
#process.load("Configuration.StandardSequences.MagneticField_0T_cff")
# 3.8T field
#process.load("Configuration.StandardSequences.MagneticField_38T_cff")
#process.prefer("VolumeBasedMagneticFieldESProducer")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
process.load("Configuration.StandardSequences.Geometry_cff")

#-------------------------------------------------
# GLOBALTAG
#-------------------------------------------------
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

#If Frontier is used in xdaq environment use the following service
#    service = SiteLocalConfigService {}

#-----------------------
#  Reconstruction Modules
#-----------------------
###process.load("Configuration.StandardSequences.Reconstruction_cff")
##process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")
# Real data raw to digi
process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
#process.load("Configuration.StandardSequences.RawToDigi_cff")
process.siPixelDigis.InputLabel = 'source'
process.siPixelDigis.IncludeErrors = True

# Local Reconstruction
process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")

#process.load("EventFilter.SiStripRawToDigi.SiStripRawToDigis_standard_cff")
#process.siStripDigis.ProductLabel = 'source'

#process.load("RecoLocalTracker.SiStripClusterizer.SiStripClusterizer_cfi")
#process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitConverter_cfi")
#process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitMatcher_cfi")
#process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTrackAngle_cfi")
#process.load("RecoLocalTracker.SiStripZeroSuppression.SiStripZeroSuppression_cfi")

#process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
#process.load("RecoPixelVertexing.Configuration.RecoPixelVertexing_cff")
##process.load("RecoLocalTracker.Configuration.RecoLocalTracker_Cosmics_cff")
#process.load("RecoTracker.Configuration.RecoTrackerP5_cff")

#----------------------------------
# High Pileup Configuration Changes
#----------------------------------
if (process.runType.getRunType() == process.runType.hpu_run):
    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_600Tower*','HLT_L1*','HLT_Jet*','HLT_*Cosmic*','HLT_HT*','HLT_MinBias_*','HLT_Physics*', 'HLT_ZeroBias*','HLT_HcalNZS*'))


process.siPixelDigis.InputLabel   = cms.InputTag("rawDataCollector")
#--------------------------------
# Heavy Ion Configuration Changes
#--------------------------------
if (process.runType.getRunType() == process.runType.hi_run):
    QTestfile = 'DQM/SiPixelMonitorClient/test/sipixel_tier0_qualitytest_heavyions.xml'
    process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
    process.load('Configuration.StandardSequences.RawToDigi_Repacked_cff')
    process.siPixelDigis.InputLabel   = cms.InputTag("rawDataRepacker")
    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_HI*'))

#--------------------------
# Pixel DQM Source and Client
#--------------------------
process.load("DQM.SiPixelCommon.SiPixelP5DQM_source_cff")
process.load("DQM.SiPixelCommon.SiPixelP5DQM_client_cff")

process.qTester = cms.EDAnalyzer("QualityTester",
    qtList = cms.untracked.FileInPath(QTestfile),
    prescaleFactor = cms.untracked.int32(1),
    getQualityTestsFromFile = cms.untracked.bool(True),
    verboseQT = cms.untracked.bool(False),
    qtestOnEndLumi = cms.untracked.bool(True),
    qtestOnEndRun = cms.untracked.bool(True)
)

process.sipixelEDAClientP5.inputSource = cms.untracked.string("rawDataCollector")
process.sipixelDaqInfo.daqSource   = cms.untracked.string("rawDataCollector")
if (process.runType.getRunType() == process.runType.hi_run):
        process.sipixelEDAClientP5.inputSource = cms.untracked.string("rawDataRepacker")
        process.sipixelDaqInfo.daqSource   = cms.untracked.string("rawDataRepacker")
#--------------------------
# Web Service
#--------------------------
process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")
process.AdaptorConfig = cms.Service("AdaptorConfig")

#--------------------------
# Filters
#--------------------------
# HLT Filter
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1

#--------------------------
# Scheduling
#--------------------------
#process.Reco = cms.Sequence(process.siPixelDigis)
process.Reco = cms.Sequence(process.siPixelDigis*process.siPixelClusters)
#process.RecoStrips = cms.Sequence(process.siStripDigis*process.siStripClusters)
#process.siPixelLocalReco = cms.Sequence(process.siPixelRecHits) 
#process.siStripLocalReco = cms.Sequence(process.siStripMatchedRecHits)
#process.trackerLocalReco = cms.Sequence(process.siPixelLocalReco*process.siStripLocalReco)
#process.trackReco = cms.Sequence(process.trackerLocalReco*process.offlineBeamSpot*process.recopixelvertexing*process.ckftracksP5) #*process.rstracks 
process.DQMmodules = cms.Sequence(process.dqmEnv*process.qTester*process.dqmSaver)

process.SiPixelDigiSource.layOn = True
process.SiPixelDigiSource.diskOn = True


process.p = cms.Path(process.Reco*process.DQMmodules*process.SiPixelRawDataErrorSource*process.SiPixelDigiSource*process.SiPixelClusterSource*process.PixelP5DQMClientWithDataCertification)
####process.p = cms.Path(process.hltTriggerTypeFilter*process.Reco*process.DQMmodules*process.SiPixelRawDataErrorSource*process.SiPixelDigiSource*process.SiPixelClusterSource*process.PixelP5DQMClientWithDataCertification)
#process.p = cms.Path(process.Reco*process.RecoStrips*process.trackReco*process.DQMmodules*process.siPixelP5DQM_cosmics_source*process.PixelP5DQMClientWithDataCertification)

#--------------------------------------------------
# Heavy Ion Specific Fed Raw Data Collection Label
#--------------------------------------------------

print "Running with run type = ", process.runType.getRunType()
