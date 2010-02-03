import FWCore.ParameterSet.Config as cms

from DQMServices.Core.DQM_cfg import *

DQM.collectorHost = 'srv-c2d05-18.cms'
DQM.collectorPort = 9090

from DQMServices.Components.DQMEnvironment_cfi import *

dqmSaver.convention = 'Online'
dqmSaver.referenceHandling = 'all'
dqmSaver.dirName = '/home/dqmdevlocal/output'
dqmSaver.producer = 'Playback'
dqmSaver.version = 2
dqmSaver.runIsComplete = True
dqmSaver.saveByTime = 1
dqmSaver.saveByLumiSection = -1
dqmSaver.saveByMinute = 4
dqmSaver.saveByRun = -1
dqmSaver.saveAtJobEnd = False
