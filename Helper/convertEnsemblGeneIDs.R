library(annotate)
library(readr)
library(dplyr)
library(biomaRt)

args = commandArgs(trailingOnly=TRUE)

print("Remove sampleID column from data and place in own vector")
data <- read_tsv(args[1])
sampleIDs <- pull(data, Sample)
data <- dplyr::select(data, -Sample)

print("Get ensemblIDs from data and place in vector")
genes <- colnames(data)

print("Get gene symbols that correspond with ensemblIDs")
mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
geneSymbols <- getBM(filters="ensembl_gene_id", attributes = c("ensembl_gene_id", "hgnc_symbol"), values = genes, mart=mart)

print("Combine symbols and IDs")
symbolsAndIDs <- c()
for (i in 1:length(genes)) {
  ensembl_ID = genes[i]

  #geneSymbol <- geneSymbols$hgnc_symbol[grepl(ensembl_ID, geneSymbols$ensembl_gene_id)]
  matching_indices = which(geneSymbols$ensembl_gene_id == ensembl_ID)
  geneSymbol <- geneSymbols$hgnc_symbol[matching_indices]

  if (len(matching_indices) > 1)
  {
    print(ensemb_ID)
    print(geneSymbol)
    stop("Cannot continue")
  }

  if (length(geneSymbol) == 0 || geneSymbol == "") {
    symbolsAndIDs[i] <- ensembl_ID
    }
  else {
    symbolsAndIDs[i] <- paste0(geneSymbol, " (", ensembl_ID, ")") 
  }
}

#print("Create list of NA symbol indices (basically those that are missing from the online database)")
#missingSymbols <- which(is.na(symbolsAndIDs))

#print("Remove columns with missing symbols from data and list of GeneSymbols")
#if (length(missingSymbols > 0)) {
#  data <- data[,-missingSymbols]
#  symbolsAndIDs <- symbolsAndIDs[-missingSymbols]
#}

print("Add sampleIDs column to front of data")
data <- cbind(sampleIDs, data)

print("Replace Ensembl ids in data with gene symbols")
colnames(data) <- c("Sample", symbolsAndIDs)
write_tsv(data, args[2])
