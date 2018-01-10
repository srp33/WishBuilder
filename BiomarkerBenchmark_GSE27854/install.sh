#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/zm3dn/download,g" -e "s,{urlClinical},https://osf.io/jhg3d/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

