server.workspace('Summary', 'DQMSummary')
server.workspace('Everything', 'DQMContent', '^')
server.workspace('CSC', 'DQMContent', '^CSC/',
                 'CSC/Layouts/00 Top Physics Efficiency',
                 'CSC/Layouts/01 Station Physics Efficiency',
		 'CSC/Layouts/02 EMU Summary/EMU Test01 - DDUs in Readout',
		 'CSC/Layouts/02 EMU Summary/EMU Test03 - DDU Reported Errors',
		 'CSC/Layouts/02 EMU Summary/EMU Test04 - DDU Format Errors',
		 'CSC/Layouts/02 EMU Summary/EMU Test05 - DDU Inputs Status',
		 'CSC/Layouts/02 EMU Summary/EMU Test06 - DDU Inputs in ERROR-WARNING State',
		 'CSC/Layouts/02 EMU Summary/EMU Test08 - CSCs Reporting Data and Unpacked',
		 'CSC/Layouts/02 EMU Summary/EMU Test10 - CSCs with Errors and Warnings (Fractions)',
		 'CSC/Layouts/02 EMU Summary/EMU Test11 - CSCs without Data Blocks')

server.workspace('DT', 'DQMContent', '^DT/',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-LocalTriggerSummary')

#server.workspace('ECAL', 'DQMContent', '^Ecal',
#                 'Ecal/Layouts/00-Global-Summary')

server.workspace('EB', 'DQMContent', '^EcalBarrel/',
                 'EcalBarrel/Layouts/00-Summary/00-Global-Summary',
                 'EcalBarrel/Layouts/00-Summary/01-Integrity-Summary',
                 'EcalBarrel/Layouts/00-Summary/02-Occupancy-Summary',
                 'EcalBarrel/Layouts/00-Summary/03-Cosmic-Summary',
                 'EcalBarrel/Layouts/00-Summary/04-PedestalOnline-Summary',
#                 'EcalBarrel/Layouts/00-Summary/05-LaserL1-Summary',
                 'EcalBarrel/Layouts/00-Summary/07-Timing-Summary',
                 'EcalBarrel/Layouts/00-Summary/08-Trigger-Summary',
                 'EcalBarrel/Layouts/00-Summary/09-Trigger-Summary')

#server.workspace('EE', 'DQMContent', '^EcalEndcap/',
#                 'EcalEndcap/Layouts/00-Summary/00-Global-Summary',
#                 'EcalEndcap/Layouts/00-Summary/01-Integrity-Summary',
#                 'EcalEndcap/Layouts/00-Summary/02-Occupancy-Summary',
#                 'EcalEndcap/Layouts/00-Summary/03-Cosmic-Summary',
#                 'EcalEndcap/Layouts/00-Summary/04-PedestalOnline-Summary',
#                 'EcalEndcap/Layouts/00-Summary/05-LaserL1-Summary',
#                 'EcalEndcap/Layouts/00-Summary/06-Led-Summary',
#                 'EcalEndcap/Layouts/00-Summary/07-Timing-Summary',
#                 'EcalEndcap/Layouts/00-Summary/08-Trigger-Summary',
#                 'EcalEndcap/Layouts/00-Summary/09-Trigger-Summary')

server.workspace('HCAL', 'DQMContent', '^Hcal',
                 'Hcal/Layouts/HCAL OverView')

server.workspace('L1T', 'DQMContent', '^L1T',
                 'L1T/Layouts/GT-Summary/algo_bits',
                 'L1T/Layouts/GMT-Summary/GMT_etaphi',
                 'L1T/Layouts/GMT-Summary/etaphi_DTCSC_and_RPC',
                 'L1T/Layouts/GMT-Summary/Regional_trigger',
                 'L1T/Layouts/GCT-Summary/IsoEmRankEtaPhiSumm',
                 'L1T/Layouts/GCT-Summary/NonIsoEmRankEtaPhiSumm',
                 'L1T/Layouts/GCT-Summary/IsoEmRank',
                 'L1T/Layouts/GCT-Summary/NonIsoEmRank',
                 'L1T/Layouts/RCT-Summary/RctIsoEmOccEtaPhi',
                 'L1T/Layouts/RCT-Summary/RctNonIsoEmOccEtaPhi',
                 'L1T/Layouts/CSCTF-Summary/CSCTF_occupancies',
                 'L1T/Layouts/DTTF-Summary/DT_TPG_phi_map',
                 'L1T/Layouts/RPCTF-Summary/RPCTF_muons_eta_phipacked')

server.workspace('RPC', 'DQMContent', '^RPC/')
server.workspace('SiStrip', 'DQMContent', '^SiStrip/',
                 'SiStrip/Layouts/SiStrip_Digi_Summary')
