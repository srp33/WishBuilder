import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

uniqueSampleIDs = set()
uniqueGeneIDs = set()

data = {}
metaColumns = []
meta = []
# Get all unique sample IDs and gene IDs
with open(inFilePath, 'r') as inFile:
    inHeaderItems = inFile.readline().rstrip("\n").split("\t")

    sampleIDIndex = inHeaderItems.index("Sample")
    for variable in inHeaderItems:
        if "gene" not in variable and "Sample" not in variable:
            metaColumns.append(inHeaderItems.index(variable))
            meta.append(variable)
    for line in inFile:
        lineItems = line.rstrip("\n").split("\t")
        data[lineItems[sampleIDIndex]] = []
        for i in range(len(lineItems)):
            if i in metaColumns:
                data[lineItems[sampleIDIndex]].append(lineItems[i])

with open(outFilePath, 'wb') as outFile:
    outText = "\t".join(["Sample", "Variable", "Value"]) + "\n"
    outFile.write(outText.encode())
    for sampleID in data.keys():
        for i in range(len(metaColumns)):
            outText = sampleID + "\t" + meta[i] + "\t" + str(data[sampleID][i]) + "\n"
            outFile.write(outText.encode())
