#!/bin/bash

# Make sure the whole script will fail if any part of it fails
set -euo pipefail

python3 parse_metadata.py "tmp.txt" "metadata.tsv.gz"
python3 parse_data.py "tmp.txt" "data.tsv.gz"
