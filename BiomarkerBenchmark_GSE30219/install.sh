#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.sh .

sed -e "s,{urlExpression},https://osf.io/g9nu4/download,g" -e "s,{urlClinical},https://osf.io/v29dy/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

