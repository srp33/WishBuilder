#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/5rjhe/download,g" -e "s,{urlClinical},https://osf.io/pu59q/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

