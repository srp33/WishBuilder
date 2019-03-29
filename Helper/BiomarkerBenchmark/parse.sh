#! /bin/bash

python3 ../Helper/BiomarkerBenchmark/parse.py tmp/*Clinical.txt tmp/*Expression.txt Gene_Expression.tsv tmp/Clinical.tsv
python3 ../Helper/convertTallFormatToWide2.py tmp/Clinical.tsv Clinical.tsv
Rscript ../Helper/mapEnsemblGeneToHGNC.R Gene_Expression.tsv Gene_Expression.tsv.aliases
