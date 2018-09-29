from sys import argv
import os

myMInFile = argv[1]
myMOutFile = argv[2]


def translate(myMInFile, myMOutFile):
    with open(myMInFile, 'r') as inFile:
        with open(myMOutFile, 'w') as outFile:
            counter = 0
            varList = set()
            myDict = {}
            for line in inFile:
                data = line.strip('\n').split('\t')
                counter += 1
                if counter == 1:
                   outFile.write((data[0]+"\t"))
                if counter != 1:
                    varList.add(data[1])
                if counter != 1 and data[0] not in myDict:
                    myDict[data[0]] = {}
            varList = sorted(list(varList))

            for key in myDict.keys():
                for item in varList:
                    myDict[key][item] = "NA"

            counter = 0
            inFile.seek(0)
            for line in inFile:
                data = line.strip('\n').split('\t')
                key = data[0]
                item = data[1]
                counter += 1
                if counter != 1:
                    myDict[key][item] = data[2]


            outFile.write(("\t".join(varList)+"\n"))

            for key in myDict.keys():
                outFile.write(key)
                for item in varList:
                    outFile.write(("\t" + myDict[key][item]))
                outFile.write("\n")


translate(myMInFile, myMOutFile)
os.remove(myMInFile)
