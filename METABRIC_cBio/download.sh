#!/bin/bash

# Because we will need to download two files, let's create a bash function that performs the steps necessary to download a file.
function downloadData {
  # This function accepts one parameter, the URL.
  # Let's assign this to a variable.
  url="$1"

  # Create a variable that parses the file name from the URL.
  fileName="$(basename $url)"

  # Check to see if the file has been downloaded already. If not, download it.
  if [ ! -f "$fileName" ]
  then
    curl -o "$fileName" -L "$url"
  fi
}

downloadData https://github.com/cBioPortal/datahub/raw/master/public/brca_metabric.tar.gz
tar -xzf brca_metabric.tar.gz
