import sys
import pandas as pd
import gzip

reference = sys.argv[1]
expression = sys.argv[2]
transposedExpression = sys.argv[3]

#reference = "tmp/Cell_Lines_Details.xlsx"
#expression = "tmp/sanger1018_brainarray_ensemblgene_rma.txt.gz"
#transposedExpression = "transposed_expression.tsv"

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
with pd.ExcelFile(reference) as openReference:
    firstSheet = openReference.parse("Cell line details")
    cellLines = firstSheet["COSMIC identifier"]
    samples = firstSheet["Sample Name"]
    for i in range(len(cellLines) - 1):
        cellLineDictionary[str(int(cellLines[i]))] = samples[i]


with open(transposedExpression, 'r') as openExpression:
    with open("Gene_Expression.tsv", 'w') as outputFile:
        lineCount = 0
        for line in openExpression:
            lineCount += 1
            if lineCount == 1:
                outputFile.write(line)
            else:
                splitLine = line.rstrip().split("\t")
                cellLine = splitLine[0]
                remainder = splitLine[1:]
                if cellLine in cellLineDictionary:
                    newLine = str(cellLineDictionary[cellLine]) + "\t" + "\t".join(remainder) + "\n"
                outputFile.write(newLine)
