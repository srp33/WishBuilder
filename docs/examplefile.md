
[parse.py](./examplefile#parsepy) | [parse.sh](./examplefile#parsesh) | [download.sh](./examplefile#downloadsh) |  [cleanup.sh](./examplefile#cleanupsh)

## parse.py

~~~~python
import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

uniqueSampleIDs = set()
uniqueGeneIDs = set()

# Get all unique sample IDs and gene IDs
with gzip.open(inFilePath, 'r') as inFile:
    inHeaderItems = inFile.readline().decode().rstrip("\n").split("\t")

    sampleIDIndex = inHeaderItems.index("icgc_donor_id")
    geneIDIndex = inHeaderItems.index("gene_id")
    countIndex = inHeaderItems.index("raw_read_count")

    numLines = 0
    for line in inFile:
        numLines += 1

        lineItems = line.decode().rstrip("\n").split("\t")
        uniqueSampleIDs.add(lineItems[sampleIDIndex])
        uniqueGeneIDs.add(lineItems[geneIDIndex])

        if numLines % 100000 == 0:
            print(numLines)

uniqueSampleIDs = sorted(list(uniqueSampleIDs))
uniqueGeneIDs = [x for x in sorted(list(uniqueGeneIDs)) if not "?" in x]

# Initialize a dictionary that will store all data values
dataDict = {}
for sampleID in uniqueSampleIDs:
    dataDict[sampleID] = {}

# Read through the file again and populate the dictionary
with gzip.open(inFilePath, 'r') as inFile:
    inFile.readline()

    numLines = 0
    for line in inFile:
        numLines += 1

        lineItems = line.decode().rstrip("\n").split("\t")
        sampleID = lineItems[sampleIDIndex]
        geneID = lineItems[geneIDIndex]
        count = lineItems[countIndex]

        dataDict[sampleID][geneID] = count

        if numLines % 100000 == 0:
            print(numLines)#with gzip.open(inFilePath, 'r') as inFile:

# Create output file
with gzip.open(outFilePath, 'wb') as outFile:
    outFile.write("\t".join(["Sample"] + uniqueGeneIDs) + "\n")

    for sampleID in uniqueSampleIDs:
        dataItems = [dataDict[sampleID][geneID] for geneID in uniqueGeneIDs]
        outFile.write("\t".join([sampleID] + dataItems) + "\n")


~~~~

## parse.sh

~~~~bash

#!/bin/bash

# Make sure the whole script will fail if any part of it fails
set -euo pipefail

python parse_metadata.py "donor.BRCA-US.tsv.gz" "metadata.tsv.gz"
python parse_data.py "exp_seq.BRCA-US.tsv.gz" "data.tsv.gz"
python keep_common_samples.py "metadata.tsv.gz" "data.tsv.gz"
~~~~
## download.sh

~~~~bash
#!/bin/bash

# Because we will need to download two files, let's create a bash function that performs the steps necessary to download a file.
function downloadData {
  # This function accepts one parameter, the URL.
  # Let's assign this to a variable.
  url="$1"

  # Create a variable that parses the file name from the URL.
  fileName="$(basename $url)"

  # Check to see if the file has been downloaded already. If not, download it.
  if [ ! -f "$fileName" ]
  then
    curl -o "$fileName" -L "$url"
  fi
}

# The data files are stored here: https://dcc.icgc.org/releases/release_25/Projects/BRCA-US
# Let's invoke the function that we just declared, for each file we want to download.
downloadData "https://dcc.icgc.org/api/v1/download?fn=/release_25/Projects/BRCA-US/donor.BRCA-US.tsv.gz"
downloadData "https://dcc.icgc.org/api/v1/download?fn=/release_25/Projects/BRCA-US/exp_seq.BRCA-US.tsv.gz"
~~~~

## cleanup.sh

~~~~bash
rm -f donor.BRCA-US.tsv.gz
rm -f exp_seq.BRCA-US.tsv.gz
rm -f *data.tsv*
~~~~
