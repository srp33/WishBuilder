#! /bin/bash

url="$1"

if [[ "$url" == "" ]]
then
  echo "No URL was specified."
  exit 1
fi

rm -rf tmp
mkdir -p tmp

cd tmp
wget -O data.tar.gz "$url"

tar -zxvf data.tar.gz
gunzip *Expression.txt.gz
