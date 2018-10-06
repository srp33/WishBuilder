#! /bin/bash

redirectedTempFolder=tmp
Expression=$redirectedTempFolder/Expression
Clinical=$redirectedTempFolder/Clinical
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFile=Gene_Expression.tsv
metadataOutFile=metadata.tsv
convertedMetaOut=Clinical.tsv

rm -f $metadataOutFile
rm -f $dataOutFile

python parse.py $Clinical $Expression $dataOutFile $metadataOutFile 
python convertTallFormatToWide2.py $metadataOutFile $convertedMetaOut
