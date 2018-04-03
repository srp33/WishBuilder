import sys, gzip

PatientCancerType = sys.argv[1]
commonValues = sys.argv[2]
outFilePath = sys.argv[3]

inCommon = []

with open(commonValues, 'r') as c:
	for line in c:
        	value = line.strip('\n').split('\t')
        	value = value[0]
        	inCommon.append(value)	

#Read in Patient Cancer Types (Sample ID's and Values)
patientIDToCancerDict = {}
with open(PatientCancerType, 'r') as f:
	for line in f:
		lineList= line.strip('\n').split('\t')
		patientIDToCancerDict[lineList[0]] = lineList[1]

# Create output file
with open(outFilePath, 'w') as outFile:
	outText = "\t".join(["Sample","Variable","Value"]) + "\n"
	outFile.write(outText)

	for cancerType in patientIDToCancerDict:
		mutation = patientIDToCancerDict[cancerType]
		sample = cancerType[:15]
		if sample in inCommon:
			outFile.write(sample + "\tSomatic mutation\t" + mutation + "\n")

