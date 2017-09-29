#!/bin/bash

# Make sure the whole script will fail if any part of it fails
set -euo pipefail

python parse_metadata.py
python parse_data.py
python keep_common_samples.py
