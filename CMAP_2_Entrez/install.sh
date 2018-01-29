#! /bin/bash

function downloadAndInstall {
  url="$1"
  fileName="$softwareFolder/$(basename $url)"

  if [ ! -f "$fileName" ];
  then
    curl -o "$fileName" -L "$url"
    bash "$fileName" -b -p "$2"
    rm "$fileName"
  fi
}

#make Software Directory
softwareFolder=Software
mkdir -p $softwareFolder

#installing miniconda
softwareName=$softwareFolder/miniconda
downloadAndInstall "https://repo.continuum.io/miniconda/Miniconda3-4.3.27.1-Linux-x86_64.sh" "$softwareName"

#setting up environment for this project
export PATH=$softwareName/bin:$PATH
conda create --name R_env pip

#install all the R packages in the environment
source activate R_env
conda install r-essentials
conda install -y -c bioconda r-sleuth 
conda install -c r r-xml=3.98_1.5
Rscript installRPackages.R
source deactivate R_env
