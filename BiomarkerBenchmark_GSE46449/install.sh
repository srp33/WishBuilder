#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/j94f8/download,g" -e "s,{urlClinical},https://osf.io/brmnx/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

