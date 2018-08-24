mkdir -p tmp

#downloading Clinical Variables
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz"
fileName=tmp/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz

wget -O $fileName $url

#downloading CancerType Samples
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FCancerType%5FSamples%2Etxt%2Egz"
fileName=tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz

wget -O $fileName $url

#downloading the raw data
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file"
fileName=tmp/GSE62944_RAW.tar

wget -O $fileName $url

cd tmp
tar -xvf GSE62944_RAW.tar

rm GSE62944_RAW.tar
