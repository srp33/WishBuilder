<h1><center>TCGA_BreastCancer_FilteredSomaticMutations_RNAExpression</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Jan 22, 18 10:01AM MST</center>


### Testing Directory . . .

#### Results: PASS
---
### Testing Configuration File . . .

&#9989;	config.yaml contains all necessary configurations.

&#9989;	Title is less than 100 characters

&#9989;	description.md contains a description.

#### Results: PASS
---
### Running Install . . .

Executing install.sh: Success

#### Results: PASS
---

### Testing file paths:

&#9989;	test_data.tsv exists.

&#9989;	test_metadata.tsv exists.

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

*Running user code . . .*

Executing download.sh: Success

Executing parse.sh: 

&#10060;	parse.sh returned an error:
~~~bash
Traceback (most recent call last):
  File "parse.py", line 53, in <module>
    adjustFile(mutectIn, mutectOut)
  File "parse.py", line 13, in adjustFile
    with gzip.open(inFile, 'r') as iF :
  File "/usr/lib/python3.5/gzip.py", line 53, in open
    binary_file = GzipFile(filename, gz_mode, compresslevel)
  File "/usr/lib/python3.5/gzip.py", line 163, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'tmp/inFiles/TCGA.BRCA.mutect.c6a029e5-0ea3-410d-9e67-360bdfee2914.DR-7.0.somatic.maf.gz'
Traceback (most recent call last):
  File "parse2.py", line 36, in <module>
    columnsOfInterest(mutectIn, mutationDict, duplicationList)
  File "parse2.py", line 10, in columnsOfInterest
    with gzip.open(inFile, 'r') as iF :
  File "/usr/lib/python3.5/gzip.py", line 53, in open
    binary_file = GzipFile(filename, gz_mode, compresslevel)
  File "/usr/lib/python3.5/gzip.py", line 163, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'tmp/outFiles/TCGA.BRCA.mutect.c6a029e5-0ea3-410d-9e67-360bdfee2914.DR-7.0.somatic_adjusted.maf.gz'
Traceback (most recent call last):
  File "parse3.py", line 76, in <module>
    with open(condensedMutationData, 'r') as f:
IOError: [Errno 2] No such file or directory: 'tmp/outFiles/condensed.maf'
~~~

