#!/bin/bash

# Make sure the whole script will fail if any part of it fails
set -euo pipefail

python3 parse_metadata.py tmp/donor.BRCA-US.tsv.gz "metadata.tsv"
python3 parse_data.py tmp/exp_seq.BRCA-US.tsv.gz "Gene_Expression.tsv"
python3 keep_common_samples.py "metadata.tsv" "Gene_Expression.tsv"
python3 ../Helper/convertTallFormatToWide2.py "metadata.tsv" "Clinical.tsv"

