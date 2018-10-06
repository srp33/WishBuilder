import gzip
import glob
import os

for file_path in glob.glob("tmp/*txt.gz"):
    with gzip.open(file_path) as gz_file:
        header_items = gz_file.readline().decode().rstrip("\n").split("\t")
        print("")
        print(os.path.basename(file_path))
        for x in header_items:
            print(x)
        print("")
