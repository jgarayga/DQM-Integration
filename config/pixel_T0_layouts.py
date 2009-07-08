def pixellayout(i, p, *rows): i["Pixel/Layouts/" + p] = DQMItem(layout=rows)

pixellayout(dqmitems, "00 - Pixel_Error_Summary",
  [{ 'path': "Pixel/AdditionalPixelErrors/SUMOFF_NErrors_FEDErrors",
     'description': "Mean number of errors per FED crate (not associated with a specific module ID - should be empty!", 
     'draw': { 'withref': "no" }}],
  [{ 'path': "Pixel/Barrel/SUMOFF_NErrors_Barrel",
     'description': "Mean number of errors per barrel module - should be empty!",
     'draw': { 'withref': "no" }}],
  [{ 'path': "Pixel/Endcap/SUMOFF_NErrors_Endcap",
     'description': "Mean number of errors per endcap module - should be empty!",
     'draw': { 'withref': "no" }}]
  )
pixellayout(dqmitems, "01 - Pixel_Digi_Summary",
  [{ 'path': "Pixel/Barrel/SUMOFF_adc_Barrel",
     'description': "Mean digi charge in ADC counts per barrel Ladder",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Barrel/SUMOFF_ndigis_Barrel",
     'description': "Mean number of digis per event per barrel Ladder",
     'draw': { 'withref': "yes" }}],
  [{ 'path': "Pixel/Endcap/SUMOFF_adc_Endcap",
     'description': "Mean digi charge in ADC counts per endcap Blade",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Endcap/SUMOFF_ndigis_Endcap",
     'description': "Mean number of digis per event per endcap Blade",
     'draw': { 'withref': "yes" }}]
  )
pixellayout(dqmitems, "02 - Pixel_Cluster_Summary",
  [{ 'path': "Pixel/Barrel/SUMOFF_charge_Barrel",
     'description': "Mean cluster charge in kilo electrons per barrel Ladder",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Barrel/SUMOFF_nclusters_Barrel",
     'description': "Mean number of clusters per event per barrel Ladder",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Barrel/SUMOFF_size_Barrel",
     'description': "Mean cluster size in number of pixels per barrel Ladder",
     'draw': { 'withref': "yes" }}],
  [{ 'path': "Pixel/Endcap/SUMOFF_charge_Endcap",
     'description': "Mean cluster charge in kilo electrons per endcap Blade",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Endcap/SUMOFF_nclusters_Endcap",
     'description': "Mean number of clusters per event per endcap Blade",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Endcap/SUMOFF_size_Endcap",
     'description': "Mean cluster size in number of pixels per barrel Blade",
     'draw': { 'withref': "yes" }}])
pixellayout(dqmitems, "03 - Pixel_Track_Summary",
  [{ 'path': "Pixel/Clusters/OnTrack/charge_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Clusters/OnTrack/size_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Clusters/OffTrack/charge_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Clusters/OffTrack/size_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Tracks/ntracks_rsWithMaterialTracksP5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
