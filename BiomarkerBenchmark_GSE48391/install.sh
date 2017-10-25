#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/c3ej4/download,g" -e "s,{urlClinical},https://osf.io/de7kg/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

