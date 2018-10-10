import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

uniqueSampleIDs = set()
uniqueGeneIDs = set()

# Get all unique sample IDs and gene IDs
with gzip.open(inFilePath, 'rb') as inFile:
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
with open(outFilePath, 'wb') as outFile:
    outText = "\t".join(["Sample"] + uniqueGeneIDs) + "\n"
    outFile.write(outText)

    for sampleID in uniqueSampleIDs:
        dataItems = [dataDict[sampleID][geneID] for geneID in uniqueGeneIDs]
        outText = "\t".join([sampleID] + dataItems) + "\n"
        outFile.write(outText)
