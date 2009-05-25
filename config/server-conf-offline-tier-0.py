import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("eb", "ee", "csc", "rpc", "hcal", "l1t", "l1temulator", "hlt", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.port        = 8030
server.serverDir   = '/data/dqm/tier-0/gui'
server.baseUrl     = '/dqm/tier-0'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Tier-0'

server.plugin('render', BASEDIR + "/style/*.cc")
server.source('DQMUnknown', 'unknown', 'DQMArchive', 8031)
server.source('DQMArchive', 'file',
              '/data/dqm/tier-0/dqm.db', '--listen 8031',
              '--load ' + server.pathOfPlugin('render'))
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/tier-0/upload')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
