#!/bin/bash

#1 is new URL, 2 is dataset number

bash cleanup.sh
bash ../Helper/newURL.sh $1
bash install.sh
bash download.sh

#Get lines from Description File3
SOURCE=$(cat newDescription | grep "Citation" -A1 | tail -n 1)


sed -e "s,{dataset},$2,g" -e "s,{source},$SOURCE,g" -e "s,{summary},"The mission of expO is to build on the technologies and outcomes of the Human Genome Project to accelerate improved clinical management of cancer patients. IGC\'s Expression Project for Oncology (expO) seeks to integrate longitudinal clinical annotation with gene expression data for a unique and powerful portrait of human malignancies, providing critical perspective on diagnostic markers, prognostic indicators, and therapeutic targets.",g"  ../Helper/BiomarkerBenchmark/description.md > description.md
