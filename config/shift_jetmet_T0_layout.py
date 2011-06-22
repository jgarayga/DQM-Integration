def shiftjetmetlayout(i, p, *rows): i["00 Shift/JetMET/" + p] = DQMItem(layout=rows)

shiftjetmetlayout(dqmitems, "00 AK5 Calo Jet Plots (for collisions)", [{ 'path': "JetMET/Jet/CleanedAntiKtJets/Pt2", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all cleaned jets (event primary vertex requirement, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" },
{ 'path': "JetMET/Jet/CleanedAntiKtJets/Constituents", 'draw': { 'withref': 'yes' }, 'description': "Number of constituents towers in the jet.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_constit_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/CleanedAntiKtJets/Phi", 'draw': { 'withref': 'yes' }, 'description': "Phi distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_phi_plots>more</a>)" },
{ 'path': "JetMET/Jet/CleanedAntiKtJets/Eta", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "01 JPT Jet Plots (for collisions)", [{ 'path': "JetMET/Jet/JPT/Pt2", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all Jet+Tracks jets (event primary vertex requirement, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" },
{ 'path': "JetMET/Jet/JPT/nTracks", 'draw': { 'withref': 'yes' }, 'description': "Number of tracks in the jet.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_constit_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/JPT/Phi", 'draw': { 'withref': 'yes' }, 'description': "Phi distribution for Jet+Tracks jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_phi_plots>more</a>)" },
{ 'path': "JetMET/Jet/JPT/Eta", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for Jet+Tracks jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "02 PF Jet Plots (for collisions)", [{ 'path': "JetMET/Jet/PFJets/Pt2", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all Particle Flow jets (event primary vertex requirement, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" },
{ 'path': "JetMET/Jet/PFJets/Constituents", 'draw': { 'withref': 'yes' }, 'description': "Number of constituents in the jet.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_constit_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/PFJets/Phi", 'draw': { 'withref': 'yes' }, 'description': "Phi distribution for Particle Flow jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_phi_plots>more</a>)" },
{ 'path': "JetMET/Jet/PFJets/Eta", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for Particle Flow jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "03 Calo MET Plots (for collisions)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMET", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" },
{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }],
[{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMEx", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mex_plots>more</a>)" },
{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMEy", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mey_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "04 PF MET Plots (for collisions)", [{ 'path': "JetMET/MET/PfMET/BasicCleanup/METTask_PfMET", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" },
{ 'path': "JetMET/MET/PfMET/BasicCleanup/METTask_PfMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }],
[{ 'path': "JetMET/MET/PfMET/BasicCleanup/METTask_PfMEx", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mex_plots>more</a>)" },
{ 'path': "JetMET/MET/PfMET/BasicCleanup/METTask_PfMEy", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mey_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "05 TC MET Plots (for collisions)", [{ 'path': "JetMET/MET/TcMET/BasicCleanup/METTask_MET", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" },
{ 'path': "JetMET/MET/TcMET/BasicCleanup/METTask_METPhi", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }],
[{ 'path': "JetMET/MET/TcMET/BasicCleanup/METTask_MEx", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mex_plots>more</a>)" },
{ 'path': "JetMET/MET/TcMET/BasicCleanup/METTask_MEy", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mey_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "06 CaloTower Plots", [{ 'path': "JetMET/CaloTowers/SchemeB/METTask_CT_emEt_ieta_iphi", 'description': "The EM Et distribution of the Calo Towers, there should not be any large holes in the plot (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#ct_emet_plots>more</a>)" }],
[{ 'path': "JetMET/CaloTowers/SchemeB/METTask_CT_hadEt_ieta_iphi", 'description': "The hadronic Et distribution of the Calo Towers, there should not be any large holes in the plot (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#ct_hadet>more</a>)" }])

def shiftjetmetcosmicslayout(i, p, *rows): i["00 Shift/JetMET/Cosmics/" + p] = DQMItem(layout=rows)


shiftjetmetcosmicslayout(dqmitems, "00 Jet Plots (for cosmics)", [{ 'path': "JetMET/Jet/AntiKtJets/Pt2", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all cleaned jets (event primary vertex requirement, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" },
{ 'path': "JetMET/Jet/AntiKtJets/Eta", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/AntiKtJets/Phi", 'draw': { 'withref': 'yes' }, 'description': "Phi distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_phi_plots>more</a>)" },
{ 'path': "JetMET/Jet/AntiKtJets/Constituents", 'draw': { 'withref': 'yes' }, 'description': "Number of constituents towers in the jet.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_constit_plots>more</a>)" }])

shiftjetmetcosmicslayout(dqmitems, "01 Calo MET Plots (for cosmics)", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMET", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" },
{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }],
[{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMEx", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mex_plots>more</a>)" },
{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMEy", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mey_plots>more</a>)" }])

shiftjetmetcosmicslayout(dqmitems, "02 PF MET Plots (for cosmics)", [{ 'path': "JetMET/MET/PfMET/All/METTask_PfMET", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" },
{ 'path': "JetMET/MET/PfMET/All/METTask_PfMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }],
[{ 'path': "JetMET/MET/PfMET/All/METTask_PfMEx", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mex_plots>more</a>)" },
{ 'path': "JetMET/MET/PfMET/All/METTask_PfMEy", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mey_plots>more</a>)" }])

shiftjetmetcosmicslayout(dqmitems, "03 TC MET Plots (for cosmics)", [{ 'path': "JetMET/MET/TcMET/All/METTask_MET", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" },
{ 'path': "JetMET/MET/TcMET/All/METTask_METPhi", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }],
[{ 'path': "JetMET/MET/TcMET/All/METTask_MEx", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mex_plots>more</a>)" },
{ 'path': "JetMET/MET/TcMET/All/METTask_MEy", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#mey_plots>more</a>)" }])

def shiftjetmethighjetlayout(i, p, *rows): i["00 Shift/JetMET/Cosmics/HighPtJet/" + p] = DQMItem(layout=rows)

shiftjetmethighjetlayout(dqmitems, "00 AK5 Calo Jet Plots (for high threshold jet triggered events)", [{ 'path': "JetMET/Jet/CleanedAntiKtJets/Pt_Hi", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all cleaned jets (event primary vertex requirement, passing high threshold single jet trigger, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/CleanedAntiKtJets/Eta_Hi", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }])

shiftjetmethighjetlayout(dqmitems, "01 PF Jet Plots (for high threshold jet triggered events)", [{ 'path': "JetMET/Jet/PFJets/Pt_Hi", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all Particle Flow jets (event primary vertex requirement, passing high threshold single jet trigger, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/PFJets/Eta_Hi", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for Particle Flow jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }])

shiftjetmethighjetlayout(dqmitems, "02 Calo MET Plots (for high threshold jet triggered events)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/HighPtJet/METTask_CaloMET", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/CaloMET/BasicCleanup/HighPtJet/METTask_CaloMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmethighjetlayout(dqmitems, "03 PF MET Plots (for high threshold jet triggered events)", [{ 'path': "JetMET/MET/PfMET/BasicCleanup/HighPtJet/METTask_PfMET", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/PfMET/BasicCleanup/HighPtJet/METTask_PfMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmethighjetlayout(dqmitems, "04 TC MET Plots (for high threshold jet triggered events)", [{ 'path': "JetMET/MET/TcMET/BasicCleanup/HighPtJet/METTask_MET", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/TcMET/BasicCleanup/HighPtJet/METTask_METPhi", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

def shiftjetmetlowjetlayout(i, p, *rows): i["00 Shift/JetMET/Cosmics/LowPtJet/" + p] = DQMItem(layout=rows)

shiftjetmetlowjetlayout(dqmitems, "00 AK5 Calo Jet Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/Jet/CleanedAntiKtJets/Pt_Hi", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all cleaned jets (event primary vertex requirement, passing low threshold single jet trigger, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/CleanedAntiKtJets/Eta_Hi", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }])

shiftjetmetlowjetlayout(dqmitems, "01 PF Jet Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/Jet/PFJets/Pt_Hi", 'draw': { 'withref': 'yes' }, 'description': "Distribution of Jet Pt for all Particle Flow jets (event primary vertex requirement, passing low threshold single jet trigger, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_pt_plots>more</a>)" }],
[{ 'path': "JetMET/Jet/PFJets/Eta_Hi", 'draw': { 'withref': 'yes' }, 'description': "Eta distribution for Particle Flow jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots#jet_eta_plots>more</a>)" }])

shiftjetmetlowjetlayout(dqmitems, "02 Calo MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/LowPtJet/METTask_CaloMET", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/CaloMET/BasicCleanup/LowPtJet/METTask_CaloMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmetlowjetlayout(dqmitems, "03 PF MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/PfMET/BasicCleanup/LowPtJet/METTask_PfMET", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/PfMET/BasicCleanup/LowPtJet/METTask_PfMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmetlowjetlayout(dqmitems, "04 TC MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/TcMET/BasicCleanup/LowPtJet/METTask_MET", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/TcMET/BasicCleanup/LowPtJet/METTask_METPhi", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

def shiftjetmethighmetlayout(i, p, *rows): i["00 Shift/JetMET/Cosmics/HighMET/" + p] = DQMItem(layout=rows)

shiftjetmethighmetlayout(dqmitems, "00 Calo MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/HighMET/METTask_CaloMET", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/CaloMET/BasicCleanup/HighMET/METTask_CaloMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmethighmetlayout(dqmitems, "01 PF MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/PfMET/BasicCleanup/HighMET/METTask_PfMET", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/PfMET/BasicCleanup/HighMET/METTask_PfMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmethighmetlayout(dqmitems, "02 TC MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/TcMET/BasicCleanup/HighMET/METTask_MET", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/TcMET/BasicCleanup/HighMET/METTask_METPhi", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

def shiftjetmetlowmetlayout(i, p, *rows): i["00 Shift/JetMET/Cosmics/LowMET/" + p] = DQMItem(layout=rows)

shiftjetmetlowmetlayout(dqmitems, "00 Calo MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/LowMET/METTask_CaloMET", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/CaloMET/BasicCleanup/LowMET/METTask_CaloMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmetlowmetlayout(dqmitems, "01 PF MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/PfMET/BasicCleanup/LowMET/METTask_PfMET", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/PfMET/BasicCleanup/LowMET/METTask_PfMETPhi", 'draw': { 'withref': 'yes' }, 'description': "The Particle Flow Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

shiftjetmetlowmetlayout(dqmitems, "02 TC MET Plots (for low threshold jet triggered events)", [{ 'path': "JetMET/MET/TcMET/BasicCleanup/LowMET/METTask_MET", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_plots>more</a>)" }],
[{ 'path': "JetMET/MET/TcMET/BasicCleanup/LowMET/METTask_METPhi", 'draw': { 'withref': 'yes' }, 'description': "The Track Corrected Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_phi_plots>more</a>)" }])

