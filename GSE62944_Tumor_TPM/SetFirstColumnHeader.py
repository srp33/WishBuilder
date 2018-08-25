import gzip, sys

inFilePath = sys.argv[1]
value = sys.argv[2]
outFilePath = sys.argv[3]

with gzip.open(inFilePath) as inFile:
    with gzip.open(outFilePath, "w") as outFile:
        inHeaderItems = inFile.readline().decode().split("\t")
        inHeaderItems[0] = value

        outFile.write(("\t".join(inHeaderItems)).encode())

        for line in inFile:
            outFile.write(line)
