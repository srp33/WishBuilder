#!/bin/bash

url="https://dcc.icgc.org/api/v1/download?fn=/current/Summary/donor.all_projects.tsv.gz"
fileName="donor.all_projects.tsv.gz"

curl -o "$fileName" -L "$url"
