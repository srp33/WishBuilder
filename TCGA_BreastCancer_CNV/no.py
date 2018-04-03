import sys

data = sys.argv[1]
common = sys.argv[2]
outfile = "notIncluded"

values = []
samples = []
nogo = []

with open(common, 'r') as v:
	for line in v:
		value = line.strip('\n').split('\t')
		value = value[0]
		values.append(value)

with open(data, 'r') as dataFile:
        samples = dataFile.readline().rstrip("\n").split("\t")
        del samples[0]

seen = {}
dupes = []

for x in values:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1

with open(outfile, 'w') as out:
	for i in dupes:
		out.write(i + "\n")


