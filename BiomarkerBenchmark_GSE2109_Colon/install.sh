#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/yh5eb/download?version=1,g" -e "s,{urlClinical},https://osf.io/jczdb/download?version=1,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

