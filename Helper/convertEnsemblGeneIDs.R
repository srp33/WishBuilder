library(annotate)
library(readr)
library(dplyr)
library(biomaRt)

args = commandArgs(trailingOnly=TRUE)

#Remove sampleID column from data and place in own vector
data <- read_tsv(args[1])
sampleIDs <- pull(data, Sample)
data <- dplyr::select(data, -Sample)

#Get ensemblIDs from data and place in vector
genes <- colnames(data)

#Get gene symbols that correspond with ensemblIDs
mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
geneSymbols <- getBM(filters="ensembl_gene_id", attributes = c("ensembl_gene_id", "hgnc_symbol"), values = genes, mart=mart)

#Combine symbols and IDs
symbolsAndIDs <- c()
for (i in 1:length(genes)) {
  geneSymbol <- geneSymbols$hgnc_symbol[grepl(genes[i], geneSymbols$ensembl_gene_id)]
  if (length(geneSymbol) == 0 || geneSymbol == "") {
    symbolsAndIDs[i] <- NA
    }
  else {
    symbolsAndIDs[i] <- paste0(geneSymbol, " (", genes[i], ")") 
  }
}

#Create list of NA symbol indices (basically those that are missing from the online database)
missingSymbols <- which(is.na(symbolsAndIDs))

#Remove columns with missing symbols from data and list of GeneSymbols
if (length(missingSymbols > 0)) {
  data <- data[,-missingSymbols]
  symbolsAndIDs <- symbolsAndIDs[-missingSymbols]
}

#Add sampleIDs column to front of data
data <- cbind(sampleIDs, data)

#Replace ensembl ids in data with genesymbols
colnames(data) <- c("Sample", symbolsAndIDs)
write_tsv(data, args[2])
