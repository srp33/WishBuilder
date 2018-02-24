import h5py
import numpy as np
import sys, gzip

sigInfoFile = sys.argv[1]
gctxFileName = sys.argv[2]
metadataOut = sys.argv[3]
dataOut = sys.argv[4]
geneFile = sys.argv[5]
cellInfo = sys.argv[6]
pertInfo = sys.argv[7]
sigMetrics = sys.argv[8]

f = h5py.File(gctxFileName, "r")


grpname = f.require_group('/0')

subgrpMeta = grpname.require_group('/0/META')
colgrp = subgrpMeta.require_group('/0/META/ROW')
rowgrp = subgrpMeta.require_group('/0/META/COL')

subgrpData = grpname.require_group('/0/DATA')
subsubgrpData = subgrpData.require_group('/0/DATA/0')


geneDict = {}
with gzip.open(geneFile, 'r') as f :
    headerLine = f.readline()

    for line in f :
        list = line.strip('\n').split('\t')
        geneDict[list[0]] = list[1]

print("writing expression file")

f = gzip.open(dataOut, 'w')
try :
    f.write("Sample")
    for value in colgrp["id"] :
        f.write('\t' + geneDict[value])
    f.write('\n')

    index = 0
    for line in subsubgrpData["matrix"] :
        a = np.asarray(line).astype(str)
        f.write(rowgrp["id"][index] + '\t' + '\t'.join(a) + '\n')
        index = index + 1 
        if index % 1000 == 0 :
            print(str(index) + " of 473647 expression")

finally :
    f.close()


print("writing metadata file")

cellHeaderList = []
cellInfoDict = {}
f = gzip.open(cellInfo, 'r')
try :
    cellHeaderList = f.readline().strip('\n').split('\t')[1:]
    for line in f :
        lineList = line.strip('\n').split('\t')
        cellInfoDict[lineList[0]] = lineList[1:]
finally:
    f.close()

pertInfoHeaderList = []
pertInfoDict = {}
f = gzip.open(pertInfo, 'r')
try :
    pertInfoHeaderList = f.readline().strip('\n').split('\t')[1:3]
    for line in f :
        lineList = line.strip('\n').split('\t')
        pertInfoDict[lineList[0]] = lineList[1:3]
finally:
    f.close()

sigMetricsHeaderList = []
sigMetricsDict = {}
f = gzip.open(sigMetrics, 'r')
try:
    firstLineList = f.readline().strip('\n').split('\t')
    sigMetricsHeaderList = firstLineList[2:4] + firstLineList[7:]
    for line in f :
        lineList = line.strip('\n').split('\t')
        sigMetricsDict[lineList[1]] = lineList[2:4] + lineList[7:]
finally:
    f.close()

sigInfo =  gzip.open(sigInfoFile, 'r')
metaOut = gzip.open(metadataOut, 'w')
try:
    headerList = sigInfo.readline().strip('\n').split('\t')
    sigId = "Sample"
    metaOut.write("Sample\tVariable\tValue\n")
    for row in sigInfo :
        rowList = row.strip('\n').split('\t')[:7]
        for i in range(len(rowList) - 1 ):
            if(str(rowList[i + 1]) != "-666") :
                metaOut.write(str(rowList[0]) + '\t' + str(headerList[i + 1]) + '\t' + str(rowList[i + 1]) + '\n')
                
                if (rowList[0] != sigId) :
                    sigMetricsList = sigMetricsDict[rowList[0]] ##This will add the sigMetrics metadata to the metadata.tsv.gz 
                    for j in range(len(sigMetricsList)) :
                        if(str(sigMetricsList[j]) != "-666") :
                            metaOut.write(str(rowList[0]) + '\t' + str(sigMetricsHeaderList[j]) + '\t' + str(sigMetricsList[j]) + '\n')
                    sigId = rowList[0]

                if (headerList[i + 1] == "cell_id") :
                    try :
                        cellIdList = cellInfoDict[rowList[i + 1]] ##This will add the cellInfo to the metadata.tsv.gz
                        for j in range(len(cellIdList)) :
                            if(str(cellIdList[j]) != "-666") :
                                metaOut.write(str(rowList[0]) + '\t' + str(cellHeaderList[j]) + '\t' + str(cellIdList[j]) + '\n')
                    except :
                        continue ## This catches SNUC4 that doesn't have any cellInfo, but is included in the sigInfo file
                elif (headerList[i + 1] == "pert_id") :
                    try :
                        pertInfoIdList = pertInfoDict[rowList[i + 1]] ##This will add the pertInfo metadata to the metadata.tsv.gz
                        for j in range(len(pertInfoIdList)) :
                            if(str(pertInfoIdList[j]) != "-666") :
                                metaOut.write(str(rowList[0]) + '\t' + str(pertInfoHeaderList[j]) + '\t' + str(pertInfoIdList[j]) + '\n')
                    except :
                        continue
finally:
    sigInfo.close()
    metaOut.close()
