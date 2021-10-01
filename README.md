# So2Sat-POP

## Visualization of the sample patches
![Upto_class13_patch_new](https://user-images.githubusercontent.com/61827990/133273367-bc32ea0c-0164-4aa1-bd21-62d2dc3fcaba.PNG)

Sample patches from the odd numbered classes of our dataset. Lower classes depicts sparsely populated areas while higher classes depicts densely populated areas.

> This figure is cited from the following paper

## Paper
https://latex.tum.de/7536525428cwvgtrcyrjds


## Data Download
### Technical University of Munich:
First version:
```
This is the first version of the So2Sat POP dataset covering 106 EU cities. 
It provides training/testing data split scenarios.
Randomly selected: 80% as train-set (80 cities) / 20% as test-set (26 cities)
DOI: 
```

## Institute
[Signal Processing in Earth Observation](https://www.asg.ed.tum.de/sipeo/home/) , Technical University of Munich, and Remote Sensing Technology Institute, German Aerospace Center.

## Funding
This research was funded by the European Research Council (ERC) under the European Unions Horizon 2020 research and innovation program with the grant number ERC-2016-StG-714087 (Acronym:  So2Sat, project website:  www.so2sat.eu), Helmholtz Association under the framework of the Helmholtz Artificial Intelligence Cooperation Unit–Local Unit “Munich Unit @Aeronautics, Space and Transport (MASTr),” and Helmholtz Excellent Professorship “Data Science in Earth Observation – Big Data Fusion for Urban Research and by the German Federal Ministry of Education and Research (BMBF) in the framework of the international future AI lab "AI4EO – Artificial Intelligence for Earth Observation: Reasoning, Uncertainties, Ethics and Beyond" (Grant number: 01DD20001). Additionally, Sugandha Doda is supported by the Helmholtz Association under the joint research school “Munich School for Data Science - MUDS”

## Description of the folders and files
### Folder Structure
![dataset](https://user-images.githubusercontent.com/61827990/133801939-eabd723f-4da7-4e3a-818f-badde7b85708.PNG)


train folder: 
```
training data folder contains 80 cities and each city folder has patches from sentinel-2 (sen2), local climate zone 
(lcz), digital elevation model, viirs nightlights (viirs), land use classifications (lu), open source maps (osm), 
osm based features in Comma Separated Value (CSV) files (osm_features) and corresponding labels(population class 
and population count) in separate CSV file for each city.
```

test folder: 
```
test data folder contains 26 cities and each city folder has patches from sentinel-2 (sen2), local climate zone 
(lcz), digital elevation model, viirs nightlights (viirs), land use classifications (lu), open source maps (osm), 
osm based features in Comma Separated Value (CSV) files (osm_features) and corresponding labels(population class 
and population count) in separate CSV file for each city.
```

Pixel size for tif file is: 10m by 10m

Other files:
 <br /> data_preprocessing.py: For each city folder creates a city_name_features.csv file, which is used for training
 <br /> rf_classification.py: Random forest classification implementation
 <br /> rf_regression.py: Random forest regression implementation

