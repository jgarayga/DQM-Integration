import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
  export YUI_ROOT=/data/sw/$SCRAM_ARCH/external/yui/2.4.1
  export QUIET_ASSERT=a
"""

server.port        = 8050
server.serverDir   = '/data/dqm/relval/gui'
server.baseUrl     = '/dqm/relval'
server.title       = 'CMS data quality'
server.serviceName = 'CERN RelVal'

server.source('DQMArchive', 'file', '/data/dqm/relval/dqm.db', '--listen 8051')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/relval/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-relval.py")
