import sys, os, optparse, re
import ROOT, xmlrpclib
 
FOLDERS     = { 
# FOLDER UNDER EvInfo        NAME    SUMMARY VALUE IN EvInfo
  'reportSummaryContents': ( 'DQM',  'reportSummary' ),
  'CertificationContents': ( 'CERT', 'CertificationSummary' ),
  'DAQContents':           ( 'DAQ',  'DAQSummary' ),
  'DCSContents':           ( 'DCS'   'DCSSummary' )
}

SUBSYSTEMS  = {
  'CSC' :        'CSC',
  'DT' :         'DT',
  'EcalBarrel' : 'ECAL',
  'EcalEndcap' : 'ECAL',
  'Hcal' :       'HCAL',
  'L1T' :        'L1T',
  'L1TEMU' :     'L1T',
  'Pixel' :      'PIX',
  'RPC' :        'RPC',
  'SiStrip' :    'STRIP'
}

def getDatasetName(file_name):
  """ Method to get dataset name from the file name"""
  d = None
  try:
    d = re.search("(__[a-zA-Z0-9-_]+)+", file_name).group(0)
    d = re.sub("__", "/", d)
  except:
    d = None
  return d

def getSummaryValues(file_name, shift_type, translate, filters = None):
  """ Method to extract keys from root file and return dict """
  ROOT.gROOT.Reset()

  run_number = None
  result = {}

  f = ROOT.TFile(file_name, 'READ')

  root = f.GetDirectory("DQMData")
  if root == None: return (run_number, result)
  
  run = None
  for key in root.GetListOfKeys():
    if re.match("^Run [0-9]+$", key.ReadObj().GetName()) and key.IsFolder():
      run_number = int(re.sub("^Run ", "", key.ReadObj().GetName()))
      run = key.ReadObj()
      break

  if run == None: return (run_number, result)

  for sub in run.GetListOfKeys():

    sub_name = sub.ReadObj().GetName()
    if not SUBSYSTEMS.has_key(sub_name): continue

    sub_key = sub_name
    if translate:
      sub_key = SUBSYSTEMS[sub_name]

    if filters != None:
      if not re.match(filters[0], sub_key):
        continue
    
    if not result.has_key(sub_key):
      result[sub_key] = {}

    evInfo = sub.ReadObj().GetDirectory("Run summary/EventInfo")
    if evInfo == None: continue

    for folder_name in FOLDERS.keys():

      folder = evInfo.GetDirectory(folder_name)
      if folder == None: continue
      
      folder_id = folder_name
      if translate:
        folder_id = FOLDERS[folder_name][0]
        if folder_id == 'DQM' and shift_type != None:
          folder_id = 'DQM ' + shift_type.upper()

      if filters != None:
        if not re.match(filters[1], folder_id):
          continue
    
      if not result[sub_key].has_key(folder_id):
        result[sub_key][folder_id] = {}

      writeValues(folder, result[sub_key][folder_id], None, filters[2])
      writeValues(evInfo, result[sub_key][folder_id], {FOLDERS[folder_name][1]: 'Summary'}, filters[2])

  f.Close()

  return (run_number, result)

def writeValues(folder, map, keymap = None, filter = None):
  """ Write values (possibly only for the keys in the keymap and filtered) from folder to map """
  for value in folder.GetListOfKeys():
    full_name = value.ReadObj().GetName()
    if not value.IsFolder() and re.match("^<.+>f=-{,1}[0-9\.]+</.+>$", full_name):
      value_name = re.sub("<(?P<n>[^>]+)>.+", "\g<n>", full_name)
      value_numb = float(re.sub("<.+>f=(?P<n>-{,1}[0-9\.]+)</.+>", "\g<n>", full_name))
      if keymap == None or keymap.has_key(value_name):
        if not keymap == None:
          if not keymap[value_name] == None:
            value_name = keymap[value_name]
        if filter == None or re.match(filter, value_name):
          if not map.has_key(value_name):
            map[value_name] = value_numb

def dict2json(d):
  """ Convert dictionary (embedded) to json string """
  s = '{'
  i = 0
  for k in d.keys():
    i = i + 1
    s = s + '"%s"=' % re.sub('"', '\\"', k)
    if type(d[k]) == type({}):
      s = s + dict2json(d[k])
    elif type(d[k]) == type(1.0) or type(d[k]) == type(1):
      s = s + str(d[k])
    else:
      s = s + '"%s"' % re.sub('"', '\\"', d[k])
    if i < len(d): s = s + ','  

  s = s + '}'
  return s

def checkFilter(raw_filter):
  """ Check if filter is OK """
  if raw_filter != None:
    try:
      filter = eval(raw_filter)
      if type("") != type(filter[0]) or type("") != type(filter[1]) or type("") != type(filter[2]):
        raise TypeError('')
    except:
      print "Bad filter value ", raw_filter, ".\nFilter should be written in python tupple with 3 elements, i.e. \"('subsystem','folder','value')\". elements are in regexp format."
      sys.exit(2)
  else:
    filter = ('.*', '.*', '.*')
  return filter
