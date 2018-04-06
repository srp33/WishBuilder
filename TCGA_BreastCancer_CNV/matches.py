#This code reads through the datafile and the metadata file, and forms a list of all the values the two hold in common


import sys, gzip, re

data = sys.argv[1]
metadata = sys.argv[2]
outfile = sys.argv[3]

shared = []
samples = []

with open(data, 'r') as dataFile:
	samples = dataFile.readline().rstrip("\n").split("\t")
	del samples[0]
#	sys.stdout.write(samples[1])

with open(metadata, 'r') as metaFile: 
	for line in metaFile:
		lineItems = line.rstrip("\n").split("\t")
		metaSample = lineItems[0][:15]
#		sys.stdout.write(metaSample)
		if metaSample in samples:
			shared.append(metaSample)
			
#shared = set(shared)
with open(outfile, 'w') as file:
	for value in shared:
		outText = value + "\n"
		file.write(outText)
