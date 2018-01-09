#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading expression data
url="https://osf.io/egh3x/download"
fileName=$redirectedTempFolder/Expression.gz

wget -O $fileName $url
gunzip $fileName

#downloading clinical data
url="https://osf.io/k9g2q/download"
fileName=$redirectedTempFolder/Clinical

wget -O $fileName $url
