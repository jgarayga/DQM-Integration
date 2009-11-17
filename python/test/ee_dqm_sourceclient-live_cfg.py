import FWCore.ParameterSet.Config as cms

import os
os.environ['TNS_ADMIN']='/etc'

dbName = ''
dbHostName = ''
dbHostPort = 1521
dbUserName = ''
dbPassword = ''

try:
  file = open('/nfshome0/ecalpro/DQM/online-DQM/.cms_tstore.conf', 'r')
  for line in file:
    if line.find('dbName') >= 0:
      dbName = line.split()[2]
    if line.find('dbHostName') >= 0:
      dbHostName = line.split()[2]
    if line.find('dbHostPort') >= 0:
      dbHostPort = int(line.split()[2])
    if line.find('dbUserName') >= 0:
      dbUserName = line.split()[2]
    if line.find('dbPassword') >= 0:
      dbPassword = line.split()[2]
  file.close()
except IOError:
  pass

process = cms.Process("ECALDQM")

process.load("DQM.Integration.test.inputsource_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")

process.load("EventFilter.EcalRawToDigi.EcalUnpackerMapping_cfi")

process.load("EventFilter.EcalRawToDigi.EcalUnpackerData_cfi")

import RecoLocalCalo.EcalRecProducers.ecalGlobalUncalibRecHit_cfi
process.ecalUncalibHit = RecoLocalCalo.EcalRecProducers.ecalGlobalUncalibRecHit_cfi.ecalGlobalUncalibRecHit.clone()

import RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi
process.ecalUncalibHit1 = RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi.ecalFixedAlphaBetaFitUncalibRecHit.clone()

import RecoLocalCalo.EcalRecProducers.ecalMaxSampleUncalibRecHit_cfi
process.ecalUncalibHit2 = RecoLocalCalo.EcalRecProducers.ecalMaxSampleUncalibRecHit_cfi.ecalMaxSampleUncalibRecHit.clone()

process.load("RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi")

process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")

process.load("Geometry.CaloEventSetup.CaloTopology_cfi")

process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.EcalMapping.EcalMapping_cfi")

process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

process.load("RecoEcal.EgammaClusterProducers.ecalClusteringSequence_cff")

process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")

process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_readDBOffline_cff")

process.load("DQM.EcalEndcapMonitorModule.EcalEndcapMonitorModule_cfi")

process.load("DQM.EcalEndcapMonitorTasks.EcalEndcapMonitorTasks_cfi")

process.load("DQM.EcalEndcapMonitorClient.EcalEndcapMonitorClient_cfi")

process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")

# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1

process.load("FWCore.Modules.preScaler_cfi")

process.ecalPhysicsFilter = cms.EDFilter("EcalMonitorPrescaler",
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    cosmicPrescaleFactor = cms.untracked.int32(1),
    physicsPrescaleFactor = cms.untracked.int32(1),
    laserPrescaleFactor = cms.untracked.int32(0),
    ledPrescaleFactor = cms.untracked.int32(0),
    pedestalPrescaleFactor = cms.untracked.int32(0),
    testpulsePrescaleFactor = cms.untracked.int32(0),
    pedestaloffsetPrescaleFactor = cms.untracked.int32(0)
)

process.ecalLaserLedFilter = cms.EDFilter("EcalMonitorPrescaler",
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    cosmicPrescaleFactor = cms.untracked.int32(0),
    physicsPrescaleFactor = cms.untracked.int32(0),
    laserPrescaleFactor = cms.untracked.int32(1),
    ledPrescaleFactor = cms.untracked.int32(1),
    pedestalPrescaleFactor = cms.untracked.int32(0),
    testpulsePrescaleFactor = cms.untracked.int32(0),
    pedestaloffsetPrescaleFactor = cms.untracked.int32(0)
)

process.ecalPedestalFilter = cms.EDFilter("EcalMonitorPrescaler",
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    cosmicPrescaleFactor = cms.untracked.int32(0),
    physicsPrescaleFactor = cms.untracked.int32(0),
    laserPrescaleFactor = cms.untracked.int32(0),
    ledPrescaleFactor = cms.untracked.int32(0),
    pedestalPrescaleFactor = cms.untracked.int32(1),
    testpulsePrescaleFactor = cms.untracked.int32(0),
    pedestaloffsetPrescaleFactor = cms.untracked.int32(1)
)

process.ecalTestPulseFilter = cms.EDFilter("EcalMonitorPrescaler",
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    cosmicPrescaleFactor = cms.untracked.int32(0),
    physicsPrescaleFactor = cms.untracked.int32(0),
    laserPrescaleFactor = cms.untracked.int32(0),
    ledPrescaleFactor = cms.untracked.int32(0),
    pedestalPrescaleFactor = cms.untracked.int32(0),
    testpulsePrescaleFactor = cms.untracked.int32(1),
    pedestaloffsetPrescaleFactor = cms.untracked.int32(0)
)

process.dqmQTestEE = cms.EDAnalyzer("QualityTester",
#    reportThreshold = cms.untracked.string('red'),
    prescaleFactor = cms.untracked.int32(4),
    qtList = cms.untracked.FileInPath('DQM/EcalEndcapMonitorModule/test/data/EcalEndcapQualityTests.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        noLineBreaks = cms.untracked.bool(True),
        noTimeStamps = cms.untracked.bool(True),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        EcalRawToDigi = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTriggerType = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTpg = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiNumTowerBlocks = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTowerSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiGainZero = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiGainSwitch = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDccBlockSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemBlock = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemGain = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTCC = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiSRP = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalDCCHeaderRuntypeDecoder = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalBarrelMonitorModule = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalEndcapMonitorModule = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        )
    ),
    categories = cms.untracked.vstring('EcalRawToDigi',
                                       'EcalRawToDigiTriggerType',
                                       'EcalRawToDigiTpg',
                                       'EcalRawToDigiNumTowerBlocks',
                                       'EcalRawToDigiTowerId',
                                       'EcalRawToDigiTowerSize',
                                       'EcalRawToDigiChId',
                                       'EcalRawToDigiGainZero',
                                       'EcalRawToDigiGainSwitch',
                                       'EcalRawToDigiDccBlockSize',
                                       'EcalRawToDigiMemBlock',
                                       'EcalRawToDigiMemTowerId',
                                       'EcalRawToDigiMemChId',
                                       'EcalRawToDigiMemGain',
                                       'EcalRawToDigiTCC',
                                       'EcalRawToDigiSRP',
                                       'EcalDCCHeaderRuntypeDecoder',
                                       'EcalBarrelMonitorModule',
                                       'EcalEndcapMonitorModule'),
    destinations = cms.untracked.vstring('cout')
)

process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")

process.preScaler.prescaleFactor = 1

process.ecalDataSequence = cms.Sequence(process.preScaler*process.ecalEBunpacker*process.ecalUncalibHit*process.ecalRecHit)

process.ecalEndcapMonitorSequence = cms.Sequence(process.ecalEndcapMonitorModule*process.ecalEndcapMonitorClient)

process.ecalEndcapMainSequence = cms.Sequence(process.ecalEndcapOccupancyTask*process.ecalEndcapIntegrityTask*process.ecalEndcapStatusFlagsTask*process.ecalEndcapRawDataTask)

process.ecalEndcapPhysicsSequence = cms.Sequence(process.ecalEndcapPedestalOnlineTask*process.ecalEndcapCosmicTask*process.ecalEndcapClusterTask*process.ecalEndcapTriggerTowerTask*process.ecalEndcapTimingTask*process.ecalEndcapSelectiveReadoutTask)

process.ecalClusterSequence = cms.Sequence(process.hybridSuperClusters*process.correctedHybridSuperClusters*process.multi5x5BasicClusters*process.multi5x5SuperClusters)

process.ecalMonitorPath = cms.Path(process.ecalDataSequence*process.ecalEndcapMonitorSequence)

process.ecalPhysicsPath = cms.Path(process.ecalDataSequence*process.hltTriggerTypeFilter*process.simEcalTriggerPrimitiveDigis*process.ecalClusterSequence*process.ecalEndcapMainSequence*process.ecalEndcapPhysicsSequence*process.ecalEndcapMainSequence*process.ecalEndcapPhysicsSequence)

process.ecalLaserLedPath = cms.Path(process.ecalDataSequence*process.ecalLaserLedFilter*process.ecalUncalibHit1*process.ecalEndcapMainSequence*process.ecalEndcapLaserTask)

process.ecalPedestalPath = cms.Path(process.ecalDataSequence*process.ecalPedestalFilter*process.ecalEndcapMainSequence*process.ecalEndcapPedestalTask)

process.ecalTestPulsePath = cms.Path(process.ecalDataSequence*process.ecalTestPulseFilter*process.ecalUncalibHit2*process.ecalEndcapMainSequence*process.ecalEndcapTestPulseTask)

process.ecalMonitorEndPath = cms.EndPath(process.dqmEnv*process.dqmQTestEE*process.dqmSaver)

process.schedule = cms.Schedule(process.ecalMonitorPath,process.ecalPhysicsPath,process.ecalLaserLedPath,process.ecalPedestalPath,process.ecalTestPulsePath,process.ecalMonitorEndPath)

process.EventStreamHttpReader.consumerName = 'EcalEndcap DQM Consumer'
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('*'))
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_Physics','HLT_EcalCalibration')
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_MinBiasEcal','HLT_L1MuOpen','HLT_EcalCalibration')

process.dqmEnv.subSystemFolder = 'EcalEndcap'

process.ecalUncalibHit.EBdigiCollection = 'ecalEBunpacker:ebDigis'
process.ecalUncalibHit.EEdigiCollection = 'ecalEBunpacker:eeDigis'

process.ecalUncalibHit1.MinAmplBarrel = 12.
process.ecalUncalibHit1.MinAmplEndcap = 16.
process.ecalUncalibHit1.EBdigiCollection = 'ecalEBunpacker:ebDigis'
process.ecalUncalibHit1.EEdigiCollection = 'ecalEBunpacker:eeDigis'

process.ecalUncalibHit2.EBdigiCollection = 'ecalEBunpacker:ebDigis'
process.ecalUncalibHit2.EEdigiCollection = 'ecalEBunpacker:eeDigis'

process.ecalRecHit.killDeadChannels = False
process.ecalRecHit.EBuncalibRecHitCollection = 'ecalUncalibHit:EcalUncalibRecHitsEB'
process.ecalRecHit.EEuncalibRecHitCollection = 'ecalUncalibHit:EcalUncalibRecHitsEE'

process.ecalEndcapCosmicTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit:EcalUncalibRecHitsEE'

process.ecalEndcapLaserTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit1:EcalUncalibRecHitsEE'
#process.ecalEndcapLaserTask.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalEndcapLaserTask.laserWavelengths = [ 1, 4 ]

process.ecalEndcapLedTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit1:EcalUncalibRecHitsEE'
process.ecalEndcapLedTask.ledWavelengths = [ 1, 2 ]
#process.ecalEndcapLedTask.ledWavelengths = [ 1 ]

#process.ecalEndcapPedestalTask.MGPAGains = [ 1, 6, 12 ]
process.ecalEndcapPedestalTask.MGPAGains = [ 12 ]
#process.ecalEndcapPedestalTask.MGPAGainsPN = [ 1, 16 ]
process.ecalEndcapPedestalTask.MGPAGainsPN = [ 16 ]

process.ecalEndcapTestPulseTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEE'
#process.ecalEndcapTestPulseTask.MGPAGains = [ 1, 6, 12 ]
process.ecalEndcapTestPulseTask.MGPAGains = [ 12 ]
#process.ecalEndcapTestPulseTask.MGPAGainsPN = [ 1, 16 ]
process.ecalEndcapTestPulseTask.MGPAGainsPN = [ 16 ]

process.ecalEndcapTimingTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit:EcalUncalibRecHitsEE'

process.simEcalTriggerPrimitiveDigis.Label = 'ecalEBunpacker'
process.simEcalTriggerPrimitiveDigis.InstanceEB = 'ebDigis'
process.simEcalTriggerPrimitiveDigis.InstanceEE = 'eeDigis'

process.ecalEndcapMonitorClient.dbName = dbName
process.ecalEndcapMonitorClient.dbHostName = dbHostName
process.ecalEndcapMonitorClient.dbHostPort = dbHostPort
process.ecalEndcapMonitorClient.dbUserName = dbUserName
process.ecalEndcapMonitorClient.dbPassword = dbPassword
process.ecalEndcapMonitorClient.dbTagName = 'CMSSW-online-central'
process.ecalEndcapMonitorClient.maskFile = ''
process.ecalEndcapMonitorClient.location = 'P5_Co'
process.ecalEndcapMonitorClient.updateTime = 4
process.ecalEndcapMonitorClient.dbUpdateTime = 120
#process.ecalEndcapMonitorClient.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalEndcapMonitorClient.laserWavelengths = [ 1, 4 ]
process.ecalEndcapMonitorClient.ledWavelengths = [ 1, 2 ]
#process.ecalEndcapMonitorClient.ledWavelengths = [ 1 ]
#process.ecalEndcapMonitorClient.MGPAGains = [ 1, 6, 12 ]
process.ecalEndcapMonitorClient.MGPAGains = [ 12 ]
#process.ecalEndcapMonitorClient.MGPAGainsPN = [ 1, 16 ]
process.ecalEndcapMonitorClient.MGPAGainsPN = [ 16 ]
process.ecalEndcapMonitorClient.enabledClients = ['Integrity', 'StatusFlags', 'Occupancy', 'PedestalOnline', 'Pedestal', 'TestPulse', 'Laser', 'Led', 'Timing', 'Cosmic', 'Cluster', 'TriggerTower', 'Summary']

process.hybridSuperClusters.HybridBarrelSeedThr = 0.150
process.hybridSuperClusters.step = 1
process.hybridSuperClusters.eseed = 0.150

process.multi5x5BasicClusters.IslandBarrelSeedThr = 0.150
process.multi5x5BasicClusters.IslandEndcapSeedThr = 0.150

process.multi5x5SuperClusters.seedTransverseEnergyThreshold = 0.150

process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/ee_reference.root'

