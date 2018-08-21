#!/bin/bash

set -euo pipefail

python3 ParseClinical.py tmp/data_clinical_patient.txt "" Patient_Characteristics.tsv.gz
python3 ParseClinical.py tmp/data_clinical_sample.txt "Sample Identifier" Sample_Characteristics.tsv.gz
python3 ParseCNA.py tmp/data_CNA.txt Copy_Number_Alterations.tsv.gz
python3 ParseMutations.py tmp/data_mutations_extended.txt
python3 ParseMutations.py tmp/data_mutations_extended.txt HGVSp HGVS_Protein_Description.tsv.gz
python3 ParseExpression.py "tmp/data_expression.txt" "Gene_Expression.tsv.gz"

python3 keep_common_samples.py *.tsv.gz

## Remove any *Variant.tsv.gz that has no Yes values
##for f in *Variant.tsv.gz
##do
##  echo $f
##  num=$(zgrep Yes $f | wc -l)
##
##  if [[ "$num" == "1" ]]
##  then
##    echo none........................
##  fi
##done

rm -f 5_prime_UTR_Variant.tsv.gz
