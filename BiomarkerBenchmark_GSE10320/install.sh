#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/2dbhv/download?version=1,g" -e "s,{urlClinical},https://osf.io/7yztd/download?version=1,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

