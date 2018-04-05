import sys

meta = sys.argv[1]
common = sys.argv[2]
genes = sys.argv[3]

inCommon = []
geneV = []

with open(common , 'r') as c:
	for line in c:
		lineItems = line.rstrip("\n").split("\t")
		item = lineItems[0]
		inCommon.append(item)


with open(meta, 'r') as m:
	for line in m:
		lineItems = line.rstrip("\n").split("\t")
		sample = lineItems[0][:15]
		gene = lineItems[1]
		if sample in inCommon:
			geneV.append(gene)
		
with open(genes,'w') as w:
	for gene in geneV:
		w.write(gene + "\n")	
