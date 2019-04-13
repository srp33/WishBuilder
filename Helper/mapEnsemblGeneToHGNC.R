library(annotate)
library(readr)
library(dplyr)
library(biomaRt)

args = commandArgs(trailingOnly=TRUE)

data = read_tsv(args[1], n_max=0)
geneIDs = colnames(data)[2:ncol(data)]

mart = useEnsembl(biomart = "ENSEMBL_MART_ENSEMBL", dataset = "hsapiens_gene_ensembl", mirror = "uswest", verbose = TRUE)

geneSymbols = getBM(filters="ensembl_gene_id", attributes = c("ensembl_gene_id", "hgnc_symbol"), values = geneIDs, mart=mart)

symbolsAndIDs = c()
symbols = c()
for (i in 1:length(geneIDs)) {
  ensembl_ID = geneIDs[i]

  matching_indices = which(geneSymbols$ensembl_gene_id == ensembl_ID)
  geneSymbol = paste(geneSymbols$hgnc_symbol[matching_indices], collapse="|")

  if (length(matching_indices) == 0 || geneSymbol == "") {
    symbolsAndIDs[i] = ensembl_ID
    symbols = ""
    }
  else {
    symbolsAndIDs[i] = paste0(geneSymbol, " (", ensembl_ID, ")") 
    symbols = geneSymbol
  }
}

colnames(data) = c("Sample", symbolsAndIDs)
write_tsv(data, args[1])

aliasData = as_tibble(cbind(symbolsAndIDs, symbols))
write_tsv(aliasData, args[2], col_names=FALSE)
