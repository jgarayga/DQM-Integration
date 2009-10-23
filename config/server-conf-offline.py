import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("castor","eb", "ee", "csc", "rpc", "hcal", "l1t", "l1temulator", "hlt", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]
LAYOUTS += ["%s/%s_T0_layouts.py" % (CONFIGDIR, x) for x in
           ("castor","pixel","sistrip","hcal", "eb", "ee", "hltmuon")]
LAYOUTS += [CONFIGDIR + "/shift_hlt_relval_layout.py"]
LAYOUTS += [CONFIGDIR + "/hlt_relval-layouts.py"]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.port        = 8080
server.serverDir   = '/data/dqm/offline/gui'
server.baseUrl     = '/dqm/offline'
server.title       = 'CMS data quality'
server.serviceName = 'Offline'

server.plugin('render', BASEDIR + "/style/*.cc")
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/offline/upload',
	      { 'offline': '/data/dqm/offline/data/ProdSys/Pass-1',
	        'ispy':   '/data/ispy-files' })
server.source('DQMUnknown', 'unknown', 8081)
server.source('DQMArchive', 'file', '/data/dqm/offline/idx', '^/Global/', '--listen 8081',
              '--load ' + server.pathOfPlugin('render'))
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
