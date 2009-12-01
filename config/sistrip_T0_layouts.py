def sistriplayout(i, p, *rows): i["SiStrip/Layouts/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "00 - ReportSummary",
 [{ 'path': "SiStrip/EventInfo/detFractionReportMap",
    'description': "Fraction of Good Detector Modules plotted in different parts of the Tracker - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "no" }},
  { 'path': "SiStrip/EventInfo/sToNReportMap",
    'description': "Accepted S/N Ratios in different parts of the Tracker. The values are 1 if the ratio is within the accepted range otherwise it is 0  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "SiStrip/EventInfo/reportSummaryMap",
    'description': "Ovelall Report Summary where detector fraction and S/N flags are combined together -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "no" }}])
sistriplayout(dqmitems, "01 - FED-Detected Errors",
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/BadActiveChannelStatusBits",
  'description': "FED IDs having connected channels, with a detected tickmark, with APV/Link errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/BadChannelStatusBits",
  'description': "FED IDs having connected channels with APV/Link Errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/AnyFEDErrors",
  'description': "FED IDs having any FED level error - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/nUnlocked",
    'description': "Number of connected channels per event being without a detected tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/nOutOfSync",
    'description': "Number of connected channels per event being out-of-sync - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/nAPVAddressError",
    'description': "Number of connected APVs per event having wrong pipeline address tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "02 - OnTrackCluster (StoN)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack_in_TIB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack_in_TOB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterStoNCorr_OnTrack_in_TID",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  {  'path':"SiStrip/MechanicalView/TEC/Summary_ClusterStoNCorr_OnTrack_in_TEC",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "03 - OffTrackCluster (Total Number)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OffTrack_in_TIB",
     'description': "Total Number of Off-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OffTrack_in_TOB",
     'description': "Total Number of Off-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_TotalNumberOfClusters_OffTrack_in_TID",
     'description': "Total Number of Off-Track clusters in TID  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  {  'path':"SiStrip/MechanicalView/TEC/Summary_TotalNumberOfClusters_OffTrack_in_TEC",
     'description': "TotalNumberOf Off-Track clusters in TEC  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "04 - Tracks ",
 [{ 'path': "Tracking/TrackParameters/NumberOfTracks_GenTk",
    'description': "Number of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/NumberOfRecHitsPerTrack_GenTk",
    'description': "Number of RecHits per Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPt_ImpactPoint_GenTk",
    'description': "Pt of Reconstructed Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "Tracking/TrackParameters/Chi2overDoF_GenTk",
    'description': "Chi Sqare per DoF  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPhi_ImpactPoint_GenTk",
    'description': "Phi distribution of Reconstructed Tracks -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackEta_ImpactPoint_GenTk",
    'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "05 - Detailed FED-Detected Errors",
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/AnyDAQProblems",
    'description': "FED IDs having DAQ problem - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/CorruptBuffers",
    'description': "FED IDs having corrupt FED buffers - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/AnyFEProblems",
    'description': "FED IDs having overflowed, missing or with bad majority address FE units - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "06 - OnTrackCluster (Total Number)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OnTrack_in_TIB",
     'description': "Total Number of On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OnTrack_in_TOB",
     'description': "Total Number of On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_TotalNumberOfClusters_OnTrack_in_TID",
     'description': "Total Number of On-Track clusters in TID  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  {  'path':"SiStrip/MechanicalView/TEC/Summary_TotalNumberOfClusters_OnTrack_in_TEC",
     'description': "TotalNumberOf On-Track clusters in TEC  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "07 - OffTrackCluster (Charge)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterCharge_OffTrack_in_TIB",
     'description': "Charge for Off-Track clusters in TIB - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterCharge_OffTrack_in_TOB",
     'description': "Charge for Off-Track clusters in TOB - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterCharge_OffTrack_in_TID",
     'description': "Charge for Off-Track clusters in TID - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}},             
   { 'path':"SiStrip/MechanicalView/TEC/Summary_ClusterCharge_OffTrack_in_TEC",
     'description': "Charge for Off-Track clusters in TEC - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}}])
sistriplayout(dqmitems, "08 - TIBSummary",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1",
     'description': "Corrected S/N ratio for TIB Layer #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2",
     'description': "Corrected S/N ratio for TIB Layer #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3",
     'description': "Corrected S/N ratio for TIB Layer #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4",
     'description': "Corrected S/N ratio for TIB Layer #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])              
sistriplayout(dqmitems, "10 - TIDFSummary",
  [{ 'path': "SiStrip/MechanicalView/TID/side_2/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__side__2__wheel__1",
     'description': "Corrected S/N ratio for TIDF Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/side_2/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__side__2__wheel__2",
     'description': "Corrected S/N ratio for TIDF Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/side_2/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__side__2__wheel__3",
     'description': "Corrected S/N ratio for TIDF Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "10 - TIDBSummary",
  [{ 'path': "SiStrip/MechanicalView/TID/side_1/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__side__1__wheel__1",
     'description': "Corrected S/N ratio for TIDB Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/side_1/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__side__1__wheel__2",
     'description': "Corrected S/N ratio for TIDB Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/side_1/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__side__1__wheel__3",
     'description': "Corrected S/N ratio for TIDB Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "11 - TOBSummary",
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1",
     'description': "Corrected S/N ratio for TOB Layer #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2",
     'description': "Corrected S/N ratio for TOB Layer #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3",
     'description': "Corrected S/N ratio for TOB Layer #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4",
     'description': "Corrected S/N ratio for TOB Layer #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5",
     'description': "Corrected S/N ratio for TOB Layer #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6",
     'description': "Corrected S/N ratio for TOB Layer #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "12 - TECFSummary",
  [{ 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__1",
     'description': "Corrected S/N ratio for TECF Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__2",
     'description': "Corrected S/N ratio for TECF Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__3",
     'description': "Corrected S/N ratio for TECF Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__4",
     'description': "Corrected S/N ratio for TECF Wheel #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__5",
     'description': "Corrected S/N ratio for TECF Wheel #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__6",
     'description': "Corrected S/N ratio for TECF Wheel #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__7",
     'description': "Corrected S/N ratio for TECF Wheel #7 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__8",
     'description': "Corrected S/N ratio for TECF Wheel #8 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__9",
     'description': "Corrected S/N ratio for TECF Wheel #9 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "13 - TECBSummary",
   [{ 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__1",
     'description': "Corrected S/N ratio for TECB Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__2",
     'description': "Corrected S/N ratio for TECB Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__3",
     'description': "Corrected S/N ratio for TECB Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__4",
     'description': "Corrected S/N ratio for TECB Wheel #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__5",
     'description': "Corrected S/N ratio for TECB Wheel #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__6",
     'description': "Corrected S/N ratio for TECB Wheel #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__7",
     'description': "Corrected S/N ratio for TECB Wheel #7 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__8",
     'description': "Corrected S/N ratio for TECB Wheel #8 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__9",
     'description': "Corrected S/N ratio for TECB Wheel #9 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])

