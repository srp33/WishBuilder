#! /bin/bash

set -o errexit

redirectedTempFolder=tmp
cellLine=$redirectedTempFolder/Cell_Lines_Details.xlsx
doseResponse=$redirectedTempFolder/v17_fitted_dose_response.xlsx
screenedComponents=$redirectedTempFolder/Screened_Compounds.xlsx
RACS=$redirectedTempFolder/RACS_in_cell_lines.xlsx
variants=$redirectedTempFolder/WES_variants.xlsx
expression=$redirectedTempFolder/sanger1018_brainarray_ensemblgene_rma.txt.gz
expressiontmp=$redirectedTempFolder/expressiontmp.tsv
dataOutFile=Gene_Expression.tsv
metadataOutFile=metadata.tsv

python3 parse.py $cellLine $doseResponse $screenedComponents $RACS $variants $expression $metadataOutFile $expressiontmp $dataOutFile 

python ../Helper/convertTallFormatToWide2.py $metadataOutFile Annotations.tsv
rm -f $metadataOutFile
