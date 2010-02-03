def l1tlayout(i, p, *rows): i["L1T/Layouts/" + p] = DQMItem(layout=rows)

def l1t_gt_single(i, dir, name):
  i["L1T/Layouts/00-GT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_gmt_single(i, dir, name):
  i["L1T/Layouts/01-GMT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_gct_single(i, dir, name):
  i["L1T/Layouts/02-GCT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

#def l1t_rct_single(i, dir, name):
#  i["L1T/Layouts/03-RCT-Summary/%s" % name] = \
#    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_csctf_single(i, dir, name):
  i["L1T/Layouts/04-CSCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

#def l1t_dttf_single(i, dir, name):
#  i["L1T/Layouts/05-DTTF-Summary/%s" % name] = DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 
def l1t_dttf_single(i, p, *rows): i["L1T/Layouts/05-DTTF-Summary/" + p] = DQMItem(layout=rows)

def l1t_rpctf_single(i, dir, name):
  i["L1T/Layouts/06-RPCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_scal_single(i, p, *rows): i["L1T/Layouts/07-SCAL4Cosmics-Summary/" + p] = DQMItem(layout=rows)

def l1t_rct_expert(i, p, *rows): i["L1T/Layouts/03-RCT-Summary/" + p] = DQMItem(layout=rows)
l1t_rct_expert(dqmitems, "RctEmIsoEmEtEtaPhi",
  [{ 'path': "L1T/L1TRCT/RctEmIsoEmEtEtaPhi", 'description': "For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "RctEmNonIsoEmEtEtaPhi",
  [{ 'path': "L1T/L1TRCT/RctEmNonIsoEmEtEtaPhi", 'description': "For description see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a>  CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "RctRegionsEtEtaPhi",
  [{ 'path': "L1T/L1TRCT/RctRegionsEtEtaPhi", 'description': "For description see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])


def l1t_summary(i, p, *rows): i["L1T/Layouts/08-L1T-Summary/" + p] = DQMItem(layout=rows)

l1t_summary(dqmitems,"00 Physics Trigger Rate",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/Physics Trigger Rate", 'description': "Physics Trigger Rate. x-axis: Time(lumisection); y-axis: Rate (Hz).  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1t_summary(dqmitems,"01 Random Trigger Rate",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/Random Trigger Rate", 'description': "Random Trigger Rate. x-axis: Time(lumisection); y-axis: Rate (Hz).  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])



# list of summary GT histograms (dqmitems, dirPath , histoName)
l1t_gt_single(dqmitems, "L1TGT", "algo_bits")
l1t_gt_single(dqmitems, "L1TGT", "tt_bits")
l1t_gt_single(dqmitems, "L1TGT", "gtfe_bx")
l1t_gt_single(dqmitems, "L1Scalers_SM", "l1AlgoBits_Vs_Bx")
l1t_gt_single(dqmitems, "L1Scalers_SM", "l1TechAlgoBits_Vs_Bx")
l1t_gt_single(dqmitems, "BXSynch", "BxOccyGtTrigType1")

# list of summary GMT histograms (dqmitems, dirPath , histoName)
l1t_gmt_single(dqmitems, "L1TGMT", "DTTF_phi")
l1t_gmt_single(dqmitems, "L1TGMT", "CSC_eta")
l1t_gmt_single(dqmitems, "L1TGMT", "RPCb_phi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_phi")
l1t_gmt_single(dqmitems, "L1TGMT", "DTTF_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "CSCTF_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "RPCb_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_etaphi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_qty")
l1t_gmt_single(dqmitems, "L1TGMT", "n_RPCb_vs_DTTF")
l1t_gmt_single(dqmitems, "L1TGMT", "Regional_trigger")

# list of summary GCT histograms (dqmitems, dirPath , histoName)
l1t_gct_single(dqmitems, "L1TGCT", "CenJetsEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "ForJetsEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "TauJetsEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "IsoEmRankEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "NonIsoEmRankEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "CenJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "ForJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "TauJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "IsoEmRank")
l1t_gct_single(dqmitems, "L1TGCT", "NonIsoEmRank")
l1t_gct_single(dqmitems, "L1TGCT", "EtMiss")
l1t_gct_single(dqmitems, "L1TGCT", "EtTotal")
l1t_gct_single(dqmitems, "L1TGCT", "EtHad")
l1t_gct_single(dqmitems, "L1TGCT", "HFRing0Corr")
l1t_gct_single(dqmitems, "L1TGCT", "HFRing1Corr")
l1t_gct_single(dqmitems, "L1TGCT", "HFTowerCountCorr")

# list of summary RCT histograms (dqmitems, dirPath , histoName)
#l1t_rct_single(dqmitems, "L1TRCT", "RctIsoEmOccEtaPhi")
#l1t_rct_single(dqmitems, "L1TRCT", "RctNonIsoEmOccEtaPhi")
#l1t_rct_single(dqmitems, "L1TRCT", "RctIsoEmRank")
#l1t_rct_single(dqmitems, "L1TRCT", "RctNonIsoEmRank")

# list of summary CSCTF histograms (dqmitems, dirPath , histoName)
l1t_csctf_single(dqmitems, "L1TCSCTF", "CSCTF_errors")
l1t_csctf_single(dqmitems, "L1TCSCTF", "CSCTF_occupancies")

# list of summary RPC histograms (dqmitems, dirPath , histoName)
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_muons_tower_phipacked")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_phi_valuepacked")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_ntrack")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_quality")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_charge_value")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_pt_value")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_bx")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCDigi_bx")

#### list of summary DTTF histograms (dqmitems, dirPath , histoName)
## l1t_dttf_single(dqmitems, "EventInfo/errorSummarySegments", "DT_TPG_phi_map")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Occupancy Summary")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Occupancy Phi vs Eta")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Phi")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Eta")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Pt")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Charge")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Quality")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated BX")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Num Tracks Per Event")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "BX Summary")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "2nd Track Summary")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Fractional High Quality Summary")

l1t_dttf_single(dqmitems, "Occupancy Summary",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Occupancy Summary", 'description' :  "DTTF occupancy plot (divided by the total number of events with a DTTF track) for each sector of each logical wheel. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
l1t_dttf_single(dqmitems, "Occupancy Phi vs Eta",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Occupancy Phi vs Eta", 'description' : "Integrated occupancy (proportionate to total number of events with a DTTF track) - phi vs eta.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
l1t_dttf_single(dqmitems, "Integrated Packed Phi",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Integrated Packed Phi", 'description' : "Integrated Paced Phi. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
l1t_dttf_single(dqmitems, "Integrated Packed Eta",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Integrated Packed Eta", 'description' : "Integrated Packed Eta. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
l1t_dttf_single(dqmitems, "Integrated Packed Pt",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Integrated Packed Pt", 'description' : "Integrated Packed Pt.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
l1t_dttf_single(dqmitems, "Integrated Packed Charge",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Integrated Packed Charge", 'description' : "Integrated Packed Charge. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
l1t_dttf_single(dqmitems, "Integrated Packed Quality",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Integrated Packed Quality", 'description' : "Integrated Packed Quality. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
l1t_dttf_single(dqmitems, "Integrated BX",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Integrated BX", 'description' : "Integrated BX plot. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
l1t_dttf_single(dqmitems, "Num Tracks Per Event",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Num Tracks Per Event", 'description' : "Integrated number of tracks per event. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
l1t_dttf_single(dqmitems, "BX Summary",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/BX Summary", 'description' : "Summary of BX's for each wheel (proportionate to total number of events with a DTTF track). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
l1t_dttf_single(dqmitems, "2nd Track Summary",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/2nd Track Summary", 'description' : "Number of 2nd tracks (proportionate to total number of events that have a DTTF track) - Sector vs Logical Wheel.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
l1t_dttf_single(dqmitems, "Fractional High Quality Summary",
               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INTEG/Fractional High Quality Summary", 'description' : "Fractional high quality (qual>3) (proportional to total bin occupancy) summary - Sector vs Logical Wheel.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\" target=\"_blank\">here</a>"}])


# list of summary SCAL histograms (dqmitems, dirPath , histoName)
l1t_scal_single(dqmitems, "Rate_AlgoBit_002",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_002", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_003",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_003", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_004",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_004", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_005",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_005", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_006",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_006", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_007",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_007", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_008",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_008", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_009",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_009", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_010",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_010", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_011",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_011", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_012",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_012", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_013",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_013", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_015",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_015", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_016",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_016", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_045",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_045", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_054",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_054", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_055",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_055", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_056",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_056", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_057",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_057", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_058",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_058", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_059",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_059", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_060",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_060", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_061",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_061", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_062",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_062", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_063",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_063", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_065",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_065", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_068",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_068", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_070",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_070", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_088",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_088", 'description' :  "none"}])


#l1tlayout(dqmitems, "GT-Summary",
#  ["L1T/L1TGT/algo_bits"])

#l1tlayout(dqmitems, "GMT-Summary",
#  ["L1T/L1TGMT/GMT_eta",
#  "L1T/L1TGMT/GMT_phi",
#  "L1T/L1TGMT/Regional_trigger"])

#l1tlayout(dqmitems, "GCT-Summary",
#          ["L1T/EventInfo/errorSummarySegments/IsoEmRankEtaPhiSumm",
#	  "L1T/EventInfo/errorSummarySegments/NonIsoEmRankEtaPhiSumm"])

#l1tlayout(dqmitems, "CSCTF-Summary",
#  ["L1T/L1TCSCTF/CSCTF_errors",
#   "L1T/L1TCSCTF/CSCTF_occupancies"])

#l1tlayout(dqmitems, "DTTF-Summary",
#  ["L1T/EventInfo/errorSummarySegments/DT_TPG_phi_map"])
