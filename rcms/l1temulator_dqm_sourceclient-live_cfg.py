import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TEmuDQMlive")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQM.Integration.test.inputsource_cfi")
process.load("DQM.Integration.test.environment_cfi")

#Please SPECIFY GLOBAL TAG for central OPERATIONS here!
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"   
process.GlobalTag.globaltag = "GR09_H_V4::All"
#process.prefer("GlobalTag")
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    

from L1Trigger.HardwareValidation.L1HardwareValidation_cff import *
newHWSequence = cms.Sequence(deEcal+deHcal+deRct+deGct+deDt+deDttf+deCsc+deCsctf+deRpc+deGmt+deGt*l1compare)
process.globalReplace("L1HardwareValidation", newHWSequence)

process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_craft_cff")
process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_craft.txt.gz'


##  Available data masks (case insensitive):
##    all, gt, muons, jets, taujets, isoem, nonisoem, met
process.l1temuEventInfoClient.dataMaskedSystems =cms.untracked.vstring("All")

##  Available emulator masks (case insensitive):
##    "all"; "dttf", "dttpg", "csctf", "csctpg", "rpc", "gmt", "ecal", "hcal", "rct", "gct", "glt"
process.l1temuEventInfoClient.emulatorMaskedSystems = cms.untracked.vstring("dttf", "dttpg", "csctf", "csctpg", "rpc", "ecal", "hcal", "rct", "glt")


#specify subsystems with qt's to be temporarily masked in summary map
#sequence: dtf,dtp,ctf,ctp,rpc,gmt, etp,htp,rct,gct,gt
#process.l1temuEventInfoClient.maskedSystems = [0,1,1,0,0,0, 0,1,0,0,1]

#replace DQMStore.referenceFileName = "L1TEMU_reference.root"
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("*")
)
process.EventStreamHttpReader.consumerName = 'L1TEMU DQM Consumer'
process.dqmEnv.subSystemFolder = 'L1TEMU'
