#!/bin/bash

set -euo pipefail

module load python/3/5
python3 parse_data.py "tmp/expression_main.txt" "tmp/probe_attributes.txt" "data.tsv.gz"
python3 parse_metadata.py "tmp/sample_attributes.txt" "tmp/metadata.tsv.gz"
