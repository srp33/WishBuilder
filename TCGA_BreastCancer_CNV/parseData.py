import sys, gzip
import numpy as np

CNVdata = sys.argv[1]
outFilePath = sys.argv[2]

#Create array and transpose 
data = []
notIncluded = ["TCGA-AC-A5EI-01","TCGA-AR-A0U1-01","TCGA-C8-A9FZ-01"]

with open(CNVdata, 'r') as f:
	for line in f:
		lineItems = line.rstrip("\n").split("\t")
		data.append(lineItems)
npArray = np.array(data)
npArray = npArray.T


firstLine = True
with open(outFilePath, 'w') as outFile:
	for line in npArray:
	#	for row in line:
		if firstLine:
			line[0] = 'Sample'
			firstLine = False
		sample = line[0]
		if sample not in notIncluded:
			#	sys.stdout.write("\t".join(line)+ '\n')
			outFile.write("\t".join(line) + '\n') 

