#!/bin/bash

python parse.py

# Let's also make sure to tell git to ignore any data files that will be created.
echo "*data.tsv*" >> .gitignore
