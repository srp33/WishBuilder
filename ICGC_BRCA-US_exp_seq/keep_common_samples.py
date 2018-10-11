import gzip, sys

inFilePath1 = sys.argv[1]
inFilePath2 = sys.argv[2]

inFile1 = open(inFilePath1, 'r')
inFile2 = open(inFilePath2, 'r')

lines1 = [line.rstrip("\n").split("\t") for line in inFile1]
lines2 = [line.rstrip("\n").split("\t") for line in inFile2]

inFile1.close()
inFile2.close()

samples1 = set([x[0] for x in lines1][1:])
samples2 = set([x[0] for x in lines2][1:])

commonSamples = samples1 & samples2

lines1 = [lineItems for lineItems in lines1 if lineItems[0] == "Sample" or lineItems[0] in commonSamples]
lines2 = [lineItems for lineItems in lines2 if lineItems[0] == "Sample" or lineItems[0] in commonSamples]

with open(inFilePath1, 'w') as outFile1:
    for lineItems in lines1:
        outText = "\t".join(lineItems) + "\n"
        outFile1.write(outText)

with open(inFilePath2, 'w') as outFile2:
    for lineItems in lines2:
        outText = "\t".join(lineItems) + "\n"
        outFile2.write(outText)
