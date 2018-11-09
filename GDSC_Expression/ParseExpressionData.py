import sys
import pandas as pd
import gzip

#reference = sys.argv[1]
#expression = sys.argv[2]
#transposedExpression = sys.argv[3]

reference = "tmp/Cell_Lines_Details.xlsx"
expression = "tmp/sanger1018_brainarray_ensemblgene_rma.txt.gz"
transposedExpression = "transposed_expression.tsv"

#transpose data
def readMatrixFromFile(filepath):
    matrix = []
    with gzip.open(filepath, 'r') as openFile:
        for line in openFile:
            matrix.append(line.decode().rstrip().split("\t"))
        return matrix

def transposeMatrix(x):
    transposed = list(zip(*x))
    for i in range(len(transposed)):
        transposed[i] = list(transposed[i])
    return transposed

def writeMatrixToFile(x, filePath):
    with open(filePath, 'w') as outFile:
        for y in x:
            outFile.write("\t".join([str(z) for z in y]) + "\n")

expressionMatrix = readMatrixFromFile(expression)
transposedMatrix = transposeMatrix(expressionMatrix)
writeMatrixToFile(transposedMatrix, transposedExpression)


#convert COSMIC identifiers to sample names
cellLineDictionary = {}
secondCellLineDictionary = {}
with pd.ExcelFile(reference) as openReference:
    firstSheet = openReference.parse("Cell line details")
    cellLines = firstSheet["COSMIC identifier"]
    samples = firstSheet["Sample Name"]
    tissueSheet = openReference.parse("COSMIC tissue classification")
    secondCellLines = tissueSheet["COSMIC_ID"]
    secondSamples = tissueSheet["Line"]
    #use -1 to ignore total row at bottom
    for i in range(len(cellLines) - 1):
        cellLineDictionary[str(int(cellLines[i]))] = samples[i]
    for i in range(len(secondCellLines)):
        secondCellLineDictionary[str(int(secondCellLines[i]))] = secondSamples[i]

expressionValueDictionary = {}
with open(transposedExpression, 'r') as openExpression:
    with open("Gene_Expression.tsv", 'w') as outputFile:
        lineCount = 0
        for line in openExpression:
            lineCount += 1
            if lineCount == 1:
                splitLine = line.rstrip().split("\t")
                outputFile.write("Sample" + "\t" + "\t".join(splitLine[1:]) + "\n")
            else:
                splitLine = line.rstrip().split("\t")
                cellLine = splitLine[0]
                remainder = splitLine[1:]
                if cellLine not in expressionValueDictionary:
                    expressionValueDictionary[cellLine] = [remainder]
                else:
                    expressionValueDictionary[cellLine].append(remainder)
        for key, val in expressionValueDictionary.items():
            writeValues = []
            if len(val) > 1:
                averagedValues = []
                for i in range(len(val[0])):
                    sum = 0
                    numItems = 0
                    for list in val:
                        sum += float(list[i])
                        numItems += 1
                    averaged = sum/numItems
                    averagedValues.append(str(averaged))
                writeValues = [averagedValues]
            else:
                writeValues = val
            if key in cellLineDictionary:
                newLine = str(cellLineDictionary[key]) + "\t" + "\t".join(writeValues[0]) + "\n"
                outputFile.write(newLine)
            elif key in secondCellLineDictionary:
                newLine = str(secondCellLineDictionary[key]) + "\t" + "\t".join(writeValues[0]) + "\n"
                outputFile.write(newLine)
            else:
                modifiedID = "COSMIC_" + key
                newLine = modifiedID + "\t" + "\t".join(writeValues[0]) + "\n"
                outputFile.write(newLine)
