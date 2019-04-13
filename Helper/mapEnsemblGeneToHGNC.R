library(annotate)
library(readr)
library(dplyr)
library(biomaRt)

args = commandArgs(trailingOnly=TRUE)

data = read_tsv(args[1])
geneIDs = colnames(data)[2:ncol(data)]

mart = useEnsembl(biomart = "ENSEMBL_MART_ENSEMBL", dataset = "hsapiens_gene_ensembl", mirror = "uswest", verbose = TRUE)

geneSymbols = getBM(filters="ensembl_gene_id", attributes = c("ensembl_gene_id", "hgnc_symbol"), values = geneIDs, mart=mart)

symbolsAndIDs = c()
aliasData = NULL
for (i in 1:length(geneIDs)) {
  ensembl_ID = geneIDs[i]

  matching_indices = which(geneSymbols$ensembl_gene_id == ensembl_ID)
  geneSymbol = paste(geneSymbols$hgnc_symbol[matching_indices], collapse="|")

  if (length(matching_indices) == 0 || geneSymbol == "") {
    symbolsAndIDs[i] = ensembl_ID
  }
  else {
    symbolAndID = paste0(geneSymbol, " (", ensembl_ID, ")")
    symbolsAndIDs[i] = symbolAndID
    aliasData = rbind(aliasData, c(symbolAndID, geneSymbol))
  }
}

colnames(data) = c("Sample", symbolsAndIDs)
write_tsv(data, args[1])

write.table(aliasData, args[2], sep="\t", quote=FALSE, col_names=NA, row.names=FALSE)
