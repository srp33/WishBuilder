#! /bin/bash

#python3 ParseCancerType.py tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz nameToAbbreviation.txt tmp/Clinical.tsv.gz
#python3 ParseClinical.py tmp/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz tmp/Clinical.tsv.gz
#python3 convertTallFormatToWide.py tmp/Clinical.tsv.gz Clinical.tsv.gz

python3 TransposeData.py tmp/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz Gene_Expression.tsv.gz
