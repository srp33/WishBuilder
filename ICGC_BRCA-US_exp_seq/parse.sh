#!/bin/bash

# Make sure the whole script will fail if any part of it fails
set -euo pipefail

python parse_metadata.py "donor.BRCA-US.tsv.gz" "metadata.tsv.gz"
python parse_data.py "exp_seq.BRCA-US.tsv.gz" "data.tsv.gz"
python keep_common_samples.py "metadata.tsv.gz" "data.tsv.gz"
