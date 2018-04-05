import sys, gzip

PatientCancerType = sys.argv[1]
commonValues = sys.argv[2]
outFilePath = sys.argv[3]

duplicates = ["TCGA-AC-A3QQ-01","TCGA-AC-A3OD-01","TCGA-A7-A26J-01","TCGA-A7-A0DB-01","TCGA-A7-A13G-01","TCGA-A7-A26I-01","TCGA-A7-A13D-01","TCGA-A7-A13E-01","TCGA-A7-A26E-01","TCGA-A7-A26F-01","TCGA-AC-A2QH-01","TCGA-A7-A0DC-01"]
inCommon = []
duplicated = []

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
		if sample in duplicates:
			duplicated.append(sample)
		if sample in inCommon and sample not in duplicated:
			outFile.write(sample + "\tSomatic mutation\t" + mutation + "\n")

