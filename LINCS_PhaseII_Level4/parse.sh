#!/bin/bash

#SBATCH --time=5:00:00   # walltime
#SBATCH --ntasks=8   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=32768M   # memory per CPU core

#Directory variables
redirectedTempFolder=tmp
createdFilesFolder=$redirectedTempFolder/Files_Created
metaDataOutFiles=$createdFilesFolder/Meta_Data
expressionDataOutFiles=$createdFilesFolder/Expression_Data
softwareFolder=Software

#Downloaded in download.sh
sigFileName=$redirectedTempFolder/GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz
gctxFileName=$redirectedTempFolder/LINCS_PhaseII_Level5.gctx
geneFile=$redirectedTempFolder/GSE70138_Broad_LINCS_gene_info_2017-03-06.txt.gz

#Downloaded and Installed in install.sh
minicondaPath=$softwareFolder/miniconda/bin/
parallelCommand=$softwareFolder/parallel-20170922/src/parallel

#Will Create
tempSigFileName=$createdFilesFolder/GSE70138_Broad_LINCS_sig_info_2017-03-06_adjusted.txt.gz
parallelFile=$createdFilesFolder/LINCS_PhaseII_Level5_parallel.txt
metaDataOutFilePrefix=$metaDataOutFiles/LINCS_PhaseII_Level5_sig_id_group_metadata_
expressionDataOutFilePrefix=$expressionDataOutFiles/LINCS_PhaseII_Level5_sig_id_group_expression_data_
tmpHeaderFile=$createdFilesFolder/header.txt
dataOutFile=data.tsv.gz
metadataOutFile=metadata.tsv.gz

#Other Metadata files that are included in final output
cellInfo=$redirectedTempFolder/GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz
pertInfo=$redirectedTempFolder/GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz
sigMetrics=$redirectedTempFolder/GSE70138_Broad_LINCS_sig_metrics_2017-03-06.txt.gz

rm -f $metadataOutFile
rm -f $dataOutFile

#Create createdFilesFolder
mkdir -p $createdFilesFolder
rm -rf $createdFilesFolder/*
mkdir -p $metaDataOutFiles
mkdir -p $expressionDataOutFiles

#miniconda is used to store panda software in environments need to activate environment
echo "Setting up environment"
cd $minicondaPath
source activate lincs_env
cd ../../..

python parse.py $sigFileName $gctxFileName $metadataOutFile $dataOutFile $geneFile $cellInfo $pertInfo $sigMetrics
