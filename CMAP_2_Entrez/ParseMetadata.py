from sys import argv
import gzip

metaDataIn = argv[1]
metaDataOut = argv[2]

with gzip.open(metaDataIn, 'r') as mdI:
    with gzip.open(metaDataOut, 'w') as mdO:
        headerItems = mdI.readline().decode().strip("\n").split("\t")

        # Remove last column name and put "Sample" at the beginning
        headerItems = ["Sample"] + headerItems[:-1]

        mdO.write(("Sample\tVariable\tValue\n").encode())

        for line in mdI:
            lineItems = line.decode().strip('\n').split('\t')

            # Remove last item and put it at the beginning
            lineItems = [lineItems[-1]] + lineItems[:-1]

            md0.write(("\t".join(lineItems) + "\n").encode())
