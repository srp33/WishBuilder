#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/78msc/download,g" -e "s,{urlClinical},https://osf.io/z2y9m/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

