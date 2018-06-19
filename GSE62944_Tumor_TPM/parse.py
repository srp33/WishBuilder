import sys, gzip
import numpy as np
from io import StringIO
import os

metadata = sys.argv[1]
patientCancerType = sys.argv[2]
tumorFeatureCounts = sys.argv[3]
dataOutFile = sys.argv[4]
metadataOutFile = sys.argv[5]
namesToAbbreviations = sys.argv[6]

def writeMetaData(ofMeta, metaDataList, code) :
    allNA = True
    notAvailableMetaVariables = []

    for i in range(len(metaDataList)) :
        metaValue = metaDataList[i].decode(code)

        if metaValue not in ["[Not Applicable]", "[Not Available]", "NA"]:
            ofMeta.write((sample  + '\t' + metadataDict["header"][i].decode(code) + '\t' + metaValue + '\n').encode())
            allNA = False
        else:
            #If all the values are [Not Available] we do not want to include them because we won't have any metavariables for the patient
            notAvailableMetaVariables.append(i)

    if allNA  == False :
        for i in notAvailableMetaVariables : #Include the metavariables if not all of them are NA, [Not Applicable], and [Not Available]
            ofMeta.write((sample  + '\t' + metadataDict["header"][i].decode(code)  + '\t' + "NA" + '\n').encode())



## Read the namesToAbbreviation
abbvToNamesDict = {}
with open(namesToAbbreviations, 'r') as f:
    f.readline()
    for line in f :
        lineList = line.strip('\n').split('\t')
        abbvToNamesDict[lineList[2]] = lineList[1]


# This code takes the new transposedNormalTPM and addes the PatientCancerType to the second column and writes it to the outFile data.tsv.gz
patientIDToCancerDict = {}
with gzip.open(patientCancerType, 'r') as f:
    for line in f:
        lineList= line.decode().strip('\n').split('\t')
        patientIDToCancerDict[lineList[0]] = lineList[1]


#store metainfo
metadataDict = {}
with gzip.open(metadata, 'r') as f :
    data = np.genfromtxt(metadata,delimiter='\t',dtype='S50')
    metadataDict["header"] = data.T[0,3:]
    for line in data.T[1:,:] :
        metadataDict[line[0]] = line[3:]


#read Tumor expression info and print out files
with gzip.open(tumorFeatureCounts, 'r') as iF:
    with gzip.open(dataOutFile, 'w') as ofData:
        with gzip.open(metadataOutFile, 'w') as ofMeta:
            counter = 0
            sampleList = []
            varList = []
            valList = []
            myDict = {}
            for line in iF:
                counter += 1
                myList = line.decode().strip('\n').split('\t')
                if counter == 1:
                    print("Generating Sample List and dictionary")
                    sampleList = myList[1:]
                    for sample in sampleList:
                        myDict[sample] = []
                else:
                    varList.append(myList[0])
                    valList = myList[1:]
                for i in range(len(valList)):
                    myDict[sampleList[i]].append(valList[i])

            ofMeta.write(("Sample\tVariable\tValue\n").encode())
            ofData.write(("Sample\t" + '\t'.join(varList) + '\n').encode())
            j = 0
            for sample in sampleList:
                j += 1
                if j % 50 == 0 :
                    print(str(j) + " of 9267")
                ofMeta.write((sample + "\tCancer_Type\t" + abbvToNamesDict[patientIDToCancerDict[sample]] + "\n").encode())
                ofData.write((sample + '\t' + "\t".join((myDict[sample])) + '\n').encode())
                metaDataList = metadataDict[sample.encode()]
                writeMetaData(ofMeta, metaDataList, 'UTF-8')

