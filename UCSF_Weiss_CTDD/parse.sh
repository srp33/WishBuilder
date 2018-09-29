#!/bin/bash

set -euo pipefail

python3 parse_data.py tmp/expression_main.txt tmp/probe_attributes.txt Gene_Expression.tsv
python3 parse_metadata.py tmp/sample_attributes.txt tmp/Metadata.tsv
python3 keep_common_samples.py tmp/Metadata.tsv Gene_Expression.tsv
python3 ../Helper/convertTallFormatToWide2.py tmp/Metadata.tsv Metadata.tsv
