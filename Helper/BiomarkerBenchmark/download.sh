#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading expression data
url="{urlExpression}"
fileName=$redirectedTempFolder/Expression.gz

wget -O $fileName $url
gunzip $fileName

#downloading clinical data
url="{urlClinical}"
fileName=$redirectedTempFolder/Clinical

wget -O $fileName $url
