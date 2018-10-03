#!/bin/bash

set -o errexit

python ParseMetadata.py tmp/GSE92742_Broad_LINCS_sig_info.txt.gz tmp/GSE92742_Broad_LINCS_cell_info.txt.gz tmp/GSE92742_Broad_LINCS_pert_info.txt.gz tmp/GSE92742_Broad_LINCS_pert_metrics.txt.gz tmp/GSE92742_Broad_LINCS_sig_metrics.txt.gz tmp/Metadata.tsv
python ../Helper/convertTallFormatToWide2.py tmp/Metadata.tsv Metadata.tsv

#python ParseExpression.py tmp/LINCS_PhaseI_Level5.gctx tmp/GSE92742_Broad_LINCS_gene_info.txt.gz Gene_Expression.tsv
