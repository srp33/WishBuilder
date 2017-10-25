#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading expression data
url="https://osf.io/4dmq8/download"
fileName=$redirectedTempFolder/Expression.gz

wget -O $fileName $url
gunzip $fileName

#downloading clinical data
url="https://osf.io/8t5fv/download"
fileName=$redirectedTempFolder/Clinical

wget -O $fileName $url
