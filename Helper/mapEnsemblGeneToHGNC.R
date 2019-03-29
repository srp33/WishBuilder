library(annotate)
library(readr)
library(dplyr)
library(biomaRt)

args = commandArgs(trailingOnly=TRUE)

dataPeek = read_tsv(args[1], n_max=0)
geneIDs = colnames(dataPeek)[2:ncol(dataPeek)]

mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
geneSymbols <- getBM(filters="ensembl_gene_id", attributes = c("ensembl_gene_id", "hgnc_symbol"), values = geneIDs, mart=mart)

symbolsAndIDs <- c()
for (i in 1:length(geneIDs)) {
  ensembl_ID = geneIDs[i]

  matching_indices = which(geneSymbols$ensembl_gene_id == ensembl_ID)
  geneSymbol <- paste(geneSymbols$hgnc_symbol[matching_indices], collapse="|")

  if (length(matching_indices) == 0 || geneSymbol == "") {
    symbolsAndIDs[i] <- ensembl_ID
    }
  else {
    symbolsAndIDs[i] <- paste0(geneSymbol, " (", ensembl_ID, ")") 
  }
}

combined <- as_tibble(cbind(geneIDs, symbolsAndIDs))

write_tsv(combined, args[2], col_names=FALSE)
