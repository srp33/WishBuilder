import h5py
import numpy as np
import sys, gzip

sigInfoFile = sys.argv[1]
gctxFileName = sys.argv[2]
metadataOut = sys.argv[3]
dataOut = sys.argv[4]
geneFile = sys.argv[5]
cellInfo = sys.argv[6]
pertInfo = sys.argv[7]
sigMetrics = sys.argv[8]

f = h5py.File(gctxFileName, "r")


grpname = f.require_group('/0')

subgrpMeta = grpname.require_group('/0/META')
colgrp = subgrpMeta.require_group('/0/META/ROW')
rowgrp = subgrpMeta.require_group('/0/META/COL')

subgrpData = grpname.require_group('/0/DATA')
subsubgrpData = subgrpData.require_group('/0/DATA/0')



print("writing expression file")

f = gzip.open(dataOut, 'w')
try :
    index = [i for i in range(len(rowgrp["id"])) if rowgrp["id"][i] == "LJP005_HA1E_24H:M01"]
    print(index)
    print(rowgrp["id"][index])
    print(subsubgrpData["matrix"][index])
#    index = 0
#    for line in subsubgrpData["matrix"] :
#        a = np.asarray(line).astype(str)
#        f.write(rowgrp["id"][index] + '\t' + '\t'.join(a) + '\n') 
#        if(rowgrp["id"][index] == "LJP005_HA1E_24H:M01") :
#            print(rowgrp["id"][index] + '\t' + '\t'.join(a) + '\n') 
#        index = index + 1 
finally :
    f.close()


