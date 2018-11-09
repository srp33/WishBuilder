import sys
import xlrd
import pandas as pd
import gzip, math

#reference = sys.argv[1]
#metadata = sys.argv[2]
#doseResponse = sys.argv[3]
#screenedCompounds = sys.argv[4]
#lnOuput = sys.argv[5]
#aucOutput = sys.argv[6]
#rmseOutput = sys.argv[7]
#racs = sys.argv[8]
#racsOutput = sys.argv[9]
#wes = sys.argv[10]
#wesOutput = sys.argv[11]

reference = "tmp/Cell_Lines_Details.xlsx"
metadata = "metadata.tsv"
doseResponse = "tmp/v17_fitted_dose_response.xlsx"
screenedCompounds = "tmp/Screened_Compounds.xlsx"
racs = "tmp/RACS_in_cell_lines.xlsx"
wes = "tmp/WES_variants.xlsx"
lnOutput = "Drug_Response_LN_IC50.tsv"
aucOutput = "Drug_Response_AUC.tsv"
rmseOutput = "Drug_Response_RMSE.tsv"
racsOutput = "RACS.tsv"
wesOutput = "Variants.tsv"

def checkIfNaN(value):
    if type(value) == float:
        if math.isnan(value) == True:
            return True
    return False

#initialize an empty dictionary for each data type
cellLineDictionary = {}
secondCellLineDictionary = {}
tissue1Dictionary = {}
tissue2Dictionary = {}
cancerTypeDictionary = {}
decodeDictionary = {}
microsatelliteDictionary = {}
screenMediumDictionary = {}
growthPropertiesDictionary = {}
siteDictionary = {}
histologyDictionary = {}
drugIDDictionary = {}
drugNameDictionary = {}

#collect data from Cell_Lines_Details.xlsx
with pd.ExcelFile(reference) as openReference:
    firstSheet = openReference.parse("Cell line details")
    decodeSheet = openReference.parse("Decode")
    tissueClassificationSheet = openReference.parse("COSMIC tissue classification")

    cellLines = firstSheet["COSMIC identifier"]
    samples = firstSheet["Sample Name"]
    tissue1 = firstSheet["GDSC\nTissue descriptor 1"]
    tissue2 = firstSheet["GDSC\nTissue\ndescriptor 2"]
    cancerType = firstSheet["Cancer Type\n(matching TCGA label)"]
    microsatellite = firstSheet["Microsatellite \ninstability Status (MSI)"]
    screenMedium = firstSheet["Screen Medium"]
    growthProperties = firstSheet["Growth Properties"]
    secondCellLines = tissueClassificationSheet["COSMIC_ID"]
    secondSamples = tissueClassificationSheet["Line"]
    site = tissueClassificationSheet["Site"]
    histology = tissueClassificationSheet["Histology"]

    #decode cancer types
    decodeAbbreviations = decodeSheet[decodeSheet.columns[0]]
    decodeDefinitions = decodeSheet[decodeSheet.columns[1]]    
    for i in range(len(decodeAbbreviations)):
        decodeDictionary[decodeAbbreviations[i]] = decodeDefinitions[i]
    cancerTypeDecoded = []
    for i in range(len(cancerType)):
        if cancerType[i] == "COAD/READ":
            cancerTypeDecoded.append("Colon adenocarcinoma and Rectum adenocarcinoma")
        elif cancerType[i] == "UNABLE TO CLASSIFY":
            cancerTypeDecoded.append("UNABLE TO CLASSIFY")
        elif checkIfNaN(cancerType[i]):
            cancerTypeDecoded.append("NA")
        else:
            cancerTypeDecoded.append(decodeDictionary[cancerType[i]])
    
    #add data to dictionaries for each data type
    #use -1 because there is a row at the bottom of the cell line sheet for totals that we want to ignore
    for i in range(len(cellLines) - 1):
        key = str(int(cellLines[i]))
        cellLineDictionary[key] = samples[i]
        tissue1Dictionary[key] = tissue1[i]
        tissue2Dictionary[key] = tissue2[i]
        cancerTypeDictionary[key] = cancerTypeDecoded[i]
        microsatelliteDictionary[key] = microsatellite[i]
        screenMediumDictionary[key] = screenMedium[i]
        growthPropertiesDictionary[key] = growthProperties[i]
        
    for i in range(len(secondCellLines)):
        key = str(int(secondCellLines[i]))
        secondCellLineDictionary[key] = secondSamples[i]
        siteDictionary[key] = site[i]
        histologyDictionary[key] = histology[i]

#compile dictionaries and header line
dictionaryList = [tissue1Dictionary, tissue2Dictionary, cancerTypeDictionary, microsatelliteDictionary, screenMediumDictionary, growthPropertiesDictionary, siteDictionary, histologyDictionary]
headerList = ["Sample", "GDSC Tissue descriptor 1", "GDSC Tissue descriptor 2", "Cancer Type", "Microsatellite instability Status", "Screen Medium", "Growth Properties", "Site", "Histology"]

#write to metadata file
with open(metadata, 'w') as outFile:
    outFile.write("\t".join(headerList) + "\n")
    for key, val in secondCellLineDictionary.items():
        valueList = []
        for dictionary in dictionaryList:
            if key in dictionary:
                valueList.append(str(dictionary[key]))
            else:
                valueList.append("NA")
        outFile.write(str(val) + "\t" + "\t".join(valueList) + "\n")

#collect data from Screened_Compounds.xlsx
drugList = []
with xlrd.open_workbook(screenedCompounds) as openScreenedCompounds:
    firstSheet = openScreenedCompounds.sheet_by_index(0)
    drugID = firstSheet.col_values(0)
    drugName = firstSheet.col_values(1)
    synonymsList = firstSheet.col_values(2)
    for i in range(1, len(drugID)):
        drugNameDictionary[drugID[i]] = drugName[i]
        drugList.append(drugName[i])
    uniqueDrugList = list(set(drugList))

def compileResponseValues(dataColumn, valueDictionary, outputFile, convertedToCellLines, convertedToDrugNames):
    for i in range(1, len(convertedToCellLines)):
        line = convertedToCellLines[i]
        drug = convertedToDrugNames[i]            
        if line in valueDictionary:
            valueDictionary[line][drug] = dataColumn[i]
        else:
            valueDictionary[line] = {drug:dataColumn[i]}
 
    with open(outputFile,'w') as openOutput:
        strDrugList = map(str, uniqueDrugList)
        openOutput.write("Sample" + "\t" + "\t".join(strDrugList) + "\n")
        for key, valDictionary in valueDictionary.items():
            floatValues = valDictionary.values()
            strValues = map(str, floatValues)
            responseValues = []
            for i in range(len(uniqueDrugList)):
                if uniqueDrugList[i] in valDictionary:
                    responseValues.append(str(valDictionary[uniqueDrugList[i]]))
                else:
                    responseValues.append("NA")
            openOutput.write(str(key) + "\t" + "\t".join(responseValues) + "\n")


#collect data from v17_fitted_dose_response.xlsx
with xlrd.open_workbook(doseResponse) as openDoseResponse:
    firstSheet = openDoseResponse.sheet_by_index(0)
    cosmic = firstSheet.col_values(2)
    ln = firstSheet.col_values(5)
    auc = firstSheet.col_values(6)
    rmse = firstSheet.col_values(7)
    drugID = firstSheet.col_values(3)

    compileLN = {}
    compileAUC = {}
    compileRMSE = {}

    convertedToCellLines = ["Sample"]
    for i in range(1, len(cosmic)):
        cosmicID = str(int(cosmic[i]))
        if cosmicID in secondCellLineDictionary:
            convertedToCellLines.append(secondCellLineDictionary[cosmicID])
        else:
            convertedToCellLines.append("COSMIC_" + cosmicID)

    convertedToDrugNames = ["Drug"]
    for i in range(1, len(drugID)):
        convertedToDrugNames.append(drugNameDictionary[drugID[i]])
 
    compileResponseValues(ln, compileLN, lnOutput, convertedToCellLines, convertedToDrugNames)
    compileResponseValues(auc, compileAUC, aucOutput, convertedToCellLines, convertedToDrugNames)
    compileResponseValues(rmse, compileRMSE, rmseOutput, convertedToCellLines, convertedToDrugNames)

#collect data from RACS_in_cell_lines.xlsx
with xlrd.open_workbook(racs) as openRACS:
    firstSheet = openRACS.sheet_by_index(0)
    cosmic = firstSheet.col_values(1)
    alterations = firstSheet.col_values(5)
    regions = firstSheet.col_values(6)
 
    samples = ["Sample"]
    for i in range(1, len(cosmic)):
        samples.append(secondCellLineDictionary[str(int(cosmic[i]))])

    compileRACS = {}
    uniqueRegions = set(regions)
    uniqueRegionsList = list(uniqueRegions)
    
    for i in range(1, len(samples)):
        line = samples[i]
        alteration = alterations[i]
        region = regions[i]
        if line in compileRACS:
            compileRACS[line][region] = alteration
        else:
            compileRACS[line] = {region:alteration}

    with open(racsOutput, 'w') as openOutput:
        openOutput.write("Sample" + "\t" + "\t".join(uniqueRegionsList) + "\n")
        for key, valDictionary in compileRACS.items():
            outputValues = []
            for i in range(len(uniqueRegionsList)):
                if uniqueRegionsList[i] in valDictionary:
                    outputValues.append(str(valDictionary[uniqueRegionsList[i]]))
                else:
                    outputValues.append("Normal")
            openOutput.write(str(key) + "\t" + "\t".join(outputValues) + "\n")            

def getSampleValue(dataDict, sample, gene, vc):
    if gene in dataDict[sample]:
        if vc in dataDict[sample][gene]:
            return "Yes"
    return "No"


#collect data from WES_variants.xlsx
with xlrd.open_workbook(wes) as openWES:
    dataSheet = openWES.sheet_by_index(1)
    cosmic = dataSheet.col_values(1)
    genes = dataSheet.col_values(3)
    classifications = dataSheet.col_values(7)

    samples = []
    for i in range(1, len(cosmic)):
        samples.append(secondCellLineDictionary[str(int(cosmic[i]))])

    genes = genes[1:]
    classifications = classifications[1:]
    
    for i in range(len(classifications)):
        if classifications[i] == "Missense":
            classifications[i] = "missense"

    compileWES = {}
    uniqueGenes = set(genes)
    uniqueGenesList = sorted(list(uniqueGenes))

    uniqueClassifications = set(classifications)
    uniqueClassificationsList = sorted(list(uniqueClassifications))

    for i in range(len(samples)):
        sample = samples[i]
        gene = genes[i]
        classification = classifications[i]
        
        if sample not in compileWES:
            compileWES[sample] = {}

        compileWES[sample][gene] = compileWES[sample].setdefault(gene, []) + [classification]


    for classification in uniqueClassificationsList:
        outFilePath = "Variant_{}.tsv".format(classification)

        classificationDictionary = {}
        classificationGenes = set()
        for sample in compileWES:
            for gene in compileWES[sample]:
                if classification in compileWES[sample][gene]:
                    classificationGenes.add(gene)

        classificationGenes = sorted(list(classificationGenes))

        with open(outFilePath, 'w') as openOutput:
            openOutput.write("\t".join(["Sample"] + classificationGenes) + "\n")

            for sample in compileWES:
                sampleList = [str(sample)] + [getSampleValue(compileWES, sample, gene, classification) for gene in classificationGenes]
                openOutput.write("\t".join(sampleList) + "\n")

