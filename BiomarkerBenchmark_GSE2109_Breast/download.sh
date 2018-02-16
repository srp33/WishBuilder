
#Downloading data
url="https://osf.io/xu28z/download?version=4"
wget -P tmp "$url"

#Dealing with Tar and Gzipped files
cd tmp
tar -xvf download?version=4 
gzip -d *Expression.txt.gz

#Renaming files to be generic names
mv *Clinical.txt Clinical
mv *Expression.txt Expression
mv *Description.md ../newDescription
#return to main directory
cd ..
