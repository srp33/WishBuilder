import gzip, sys

inFilePath = sys.argv[1]
value = sys.argv[2]
outFilePath = sys.argv[3]

with open(inFilePath) as inFile:
    with open(outFilePath, "w") as outFile:
        inHeaderItems = inFile.readline().split("\t")
        inHeaderItems[0] = value

        outFile.write(("\t".join(inHeaderItems)))

        for line in inFile:
            outFile.write(line)
