def shifteelayout(i, p, *rows): i["00 Shift/EcalEndcap/" + p] = DQMItem(layout=rows)

shifteelayout(dqmitems, "00 Report Summary",
  [{ 'path': "EcalEndcap/EventInfo/reportSummaryMap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "01 Event Type",
  [{ 'path': "EcalEndcap/EcalInfo/EVTTYPE", 'description': "Frequency of the event types found in the DQM event-stream. If the calibration sequence is ON, histograms should show entries in COSMICS_GLOBAL, LASER_GAP, PEDESTAL_GAP, TESTPULSE_GAP. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "02 Integrity Summary",
  [{ 'path': "EcalEndcap/EESummaryClient/EEIT EE - integrity quality summary", 'description': "Integrity quality summary. Expected all green color. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EEIT EE + integrity quality summary", 'description': "Integrity quality summary. Expected all green color. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "03 StatusFlags Summary",
  [{ 'path': "EcalEndcap/EESummaryClient/EESFT EE - front-end status summary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EESFT EE + front-end status summary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "04 PedestalOnline RMS",
  [{ 'path': "EcalEndcap/EESummaryClient/EEPOT EE - pedestal G12 RMS map", 'description': "RMS of the pedestals in ADC counts. Pedestal is evaluated using the first 3/10 samples of the pulse shape for all the events (calibration and physics). Expected RMS for ECAL endcap is 1.9 ADC counts (120 MeV). <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EEPOT EE + pedestal G12 RMS map", 'description': "RMS of the pedestals in ADC counts. Pedestal is evaluated using the first 3/10 samples of the pulse shape for all the events (calibration and physics). Expected RMS for ECAL endcap is 1.9 ADC counts (120 MeV). <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "05 Occupancy Rechits EE -",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE -", 'description': "Map of the occupancy of ECAL calibrated reconstructed hits. Expect uniform color. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE - projection eta", 'description': "Eta projection of the occupancy of ECAL calibrated reconstructed hits. Expect uniform distribution. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE - projection phi", 'description': "Phi projection of the occupancy of ECAL calibrated reconstructed hits. Expect uniform distribution. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "05 Occupancy Rechits EE +",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE +", 'description': "Map of the occupancy of ECAL calibrated reconstructed hits. Expect uniform color. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE + projection eta", 'description': "Eta projection of the occupancy of ECAL calibrated reconstructed hits. Expect uniform distribution. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE + projection phi", 'description': "Phi projection of the occupancy of ECAL calibrated reconstructed hits. Expect uniform distribution. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "06 Occupancy Trigger Primitives EE -",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE -", 'description': "Map of the occupancy of ECAL trigger primitives with energy > 4 ADC counts (~1 GeV). Expect uniform color. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE - projection eta", 'description': "Eta projection of the occupancy of ECAL trigger primitives with energy > 4 ADC counts (~1 GeV). <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE - projection phi", 'description': "Phi projection of the occupancy of ECAL trigger primitives with energy > 4 ADC counts (~1 GeV). Expect uniform distribution. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "06 Occupancy Trigger Primitives EE +",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE +", 'description': "Map of the occupancy of ECAL trigger primitives with energy > 4 ADC counts (~1 GeV). Expect uniform color. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE + projection eta", 'description': "Eta projection of the occupancy of ECAL trigger primitives with energy > 4 ADC counts (~1 GeV). <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE + projection phi", 'description': "Phi projection of the occupancy of ECAL trigger primitives with energy > 4 ADC counts (~1 GeV). Expect uniform distribution. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "07 Clusters Energy EE -",
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE -", 'description': "Average energy (in GeV) of 5x5 basic clusters. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection eta EE -", 'description': "Eta projection of 5x5 basic clusters. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE -", 'description': "phi projection of 5x5 basic clusters. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "07 Clusters Energy EE +",
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE +", 'description': "Average energy (in GeV) of 5x5 basic clusters. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection eta EE +", 'description': "Eta projection of 5x5 basic clusters. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE +", 'description': "phi projection of 5x5 basic clusters. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "08 LaserL1 Quality",
  [{ 'path': "EcalEndcap/EESummaryClient/EELT EE - laser quality summary L1", 'description': "Quality summary of laser events. Expect green where the laser sequence fired, yellow elsewhere. Red spots are failed channels. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EELT EE + laser quality summary L1", 'description': "Quality summary of laser events. Expect green where the laser sequence fired, yellow elsewhere. Red spots are failed channels. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "09 LedL1 Quality", 
  [{ 'path': "EcalEndcap/EESummaryClient/EELDT EE - led quality summary L1", 'description': "Quality summary of led events. Expect green where the laser sequence fired, yellow elsewhere. Red spots are failed channels. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }], 
  [{ 'path': "EcalEndcap/EESummaryClient/EELDT EE + led quality summary L1", 'description': "Quality summary of led events. Expect green where the laser sequence fired, yellow elsewhere. Red spots are failed channels. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "10 Pedestal Gain12 Quality",
  [{ 'path': "EcalEndcap/EESummaryClient/EEPT EE - pedestal quality G12 summary", 'description': "Quality summary of pedestal events for Gain 12. Expect green where the pedestal sequence fired, yellow elsewhere. Red spots are failed channels. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EEPT EE + pedestal quality G12 summary", 'description': "Quality summary of pedestal events for Gain 12. Expect green where the pedestal sequence fired, yellow elsewhere. Red spots are failed channels. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "11 TestPulse Gain12 Quality",
  [{ 'path': "EcalEndcap/EESummaryClient/EETPT EE - test pulse quality G12 summary", 'description': "Quality summary of test pulse events for Gain 12. Expect green where the calibration sequence fired, yellow elsewhere. Red spots are failed channels. Sectors are filled as the calibration sequence reach them: expected all yellow at beginning of run, then becoming green sector by sector. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EETPT EE + test pulse quality G12 summary", 'description': "Quality summary of test pulse events for Gain 12. Expect green where the calibration sequence fired, yellow elsewhere. Red spots are failed channels. Sectors are filled as the calibration sequence reach them: expected all yellow at beginning of run, then becoming green sector by sector. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])
