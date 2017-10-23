#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/z9t58/download,g" -e "s,{urlClinical},https://osf.io/75fwy/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

