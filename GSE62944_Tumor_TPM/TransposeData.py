import gzip, os, sys

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

print("Reading data from {}".format(inFilePath))
data = []
with gzip.open(inFilePath) as inFile:
    for line in inFile:
        data.append(line.decode().rstrip().split("\t"))

print("Transposing data from {}".format(inFilePath))
transposed = zip(*data)

print("Writing data to {}".format(outFilePath))
with gzip.open(outFilePath, 'w') as outFile:
    for lineItems in transposed:
        outFile.write(("\t".join(lineItems) + "\n").encode())
