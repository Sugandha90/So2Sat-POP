# So2Sat-POP

## Visualization of the sample patches
![Upto_class13_patch_new](https://user-images.githubusercontent.com/61827990/133273367-bc32ea0c-0164-4aa1-bd21-62d2dc3fcaba.PNG)

> This figure is cited from the following paper

## Paper
https://latex.tum.de/7536525428cwvgtrcyrjds


## Data Download
### Technical University of Munich:
First version:
```
This is the first version of the So2Sat POP dataset covering 106 EU cities. It provides training/testing data split scenarios:
Randomly selected: 80% as train-set (80 cities) / 20% as test-set (26 cities)
DOI
```

## Institute
[Signal Processing in Earth Observation](https://www.asg.ed.tum.de/sipeo/home/) , Technical University of Munich, and Remote Sensing Technology Institute, German Aerospace Center.

## Funding
This work is funded by European Research Council starting Grant:
ERC-2016-StG-714087 (Acronym:  So2Sat, project website:  www.so2sat.eu)

## Description of the folders and files
### Folder Structure
![folder_structure](https://user-images.githubusercontent.com/61827990/133273525-7dfe0edb-e792-4915-936c-33cbd0e43822.PNG)

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
