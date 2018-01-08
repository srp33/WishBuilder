#! /bin/bash

redirectedTempFolder=tmp
metaData=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt
patientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt
tumorTPM=$redirectedTempFolder/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt
transposedTumorTPM=$redirectedTempFolder/transposedTumorTPM.txt
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

rm -f $metadataOutFilegz
rm -f $dataOutFilegz

python parse.py $metaData $patientCancerType $tumorTPM $transposedTumorTPM $dataOutFile $metadataOutFile

gzip $metadataOutFile
gzip $dataOutFile
