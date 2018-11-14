#! /bin/bash

python3 ../Helper/BiomarkerBenchmark/parse.py tmp/*Clinical.txt tmp/*Expression.txt tmp/Gene_Expression.tsv tmp/Clinical.tsv
python3 ../Helper/convertTallFormatToWide2.py tmp/Clinical.tsv Clinical.tsv
Rscript ../Helper/convertEnsemblGeneIDs.R tmp/Gene_Expression.tsv Gene_Expression.tsv
