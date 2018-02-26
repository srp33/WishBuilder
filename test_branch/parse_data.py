import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

uniqueSampleIDs = set()
uniqueGeneIDs = set()

data = {}
geneColumns = []
genes = []
# Get all unique sample IDs and gene IDs
with open(inFilePath, 'r') as inFile:
    inHeaderItems = inFile.readline().rstrip("\n").split("\t")

    sampleIDIndex = inHeaderItems.index("Sample")
    for variable in inHeaderItems:
        if "gene" in variable:
            geneColumns.append(inHeaderItems.index(variable))
            genes.append(variable)
    for line in inFile:
        lineItems = line.rstrip("\n").split("\t")
        data[lineItems[sampleIDIndex]] = []
        for i in range(len(lineItems)):
            if i in geneColumns:
                data[lineItems[sampleIDIndex]].append(lineItems[i])

with gzip.open(outFilePath, 'wb') as outFile:
    outText = "\t".join(["Sample"] + genes) + "\n"
    outFile.write(outText.encode())
    for sampleID in data.keys():
        outText = "\t".join([sampleID] + data[sampleID]) + "\n"
        outFile.write(outText.encode())
