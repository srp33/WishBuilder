#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/4dmq8/download,g" -e "s,{urlClinical},https://osf.io/8t5fv/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

