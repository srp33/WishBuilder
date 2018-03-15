#! /bin/bash

redirectedTemp=tmp
inFiles=$redirectedTemp/inFiles
mkdir -p $redirectedTemp
mkdir -p $inFiles

cd $inFiles

url="https://api.gdc.cancer.gov/data/c6a029e5-0ea3-410d-9e67-360bdfee2914"
fileName=afile
wget -O $fileName $url
gunzip $fileName

#downloading CancerType Samples
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FCancerType%5FSamples%2Etxt%2Egz"
fileName=GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz

wget -O $fileName $url
gunzip $fileName

