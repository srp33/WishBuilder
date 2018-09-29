#!/bin/bash

set -euo pipefail

python3 parse_data.py "tmp/expression_main.txt" "tmp/probe_attributes.txt" "data.tsv"
python3 parse_metadata.py "tmp/sample_attributes.txt" "metadata.tsv"
python3 keep_common_samples.py "metadata.tsv" "data.tsv"
python3 ../Helper/convertTallFormatToWide2.py "metadata.tsv" "Clinical.tsv"
