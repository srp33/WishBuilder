#! /bin/bash

dataIn=tmp/Matrices/CMap_SCAN_EntrezGene_BatchAdjusted.tsv.gz
convertedData=tmp/test.tsv
metaDataIn=tmp/CMAP_Metadata.tsv

python3 parse.py $convertedData $metaDataIn $dataOut tmp/Metadata.tsv.gz
python3 convertTallFormatToWide.py tmp/Metadata.tsv.gz Metadata.tsv.gz

Rscript entrezIdConvert.R tmp/Matrices/CMap_SCAN_EntrezGene_BatchAdjusted.tsv.gz Gene_Expression.tsv.gz
