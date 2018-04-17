<h1><center>TCGA_BreastCancer_DNAMethylation</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Apr 17, 18 11:04AM MST</center>


### Testing Directory . . .

#### Results: PASS
---
### Testing Configuration File . . .

&#9989;	config.yaml contains all necessary configurations.

&#9989;	Title is less than 300 characters

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

Executing download.sh: 

&#10060;	download.sh returned an error:
~~~bash
--2018-04-17 18:56:54--  https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FCancerType%5FSamples%2Etxt%2Egz
Resolving www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)... 130.14.29.110, 2607:f220:41e:4290::110
Connecting to www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)|130.14.29.110|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 73327 (72K) [application/octet-stream]
Saving to: ‘tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz’

     0K .......... .......... .......... .......... .......... 69%  474K 0s
    50K .......... .......... .                               100% 33.2M=0.1s

2018-04-17 18:56:54 (675 KB/s) - ‘tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz’ saved [73327/73327]

gzip: tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt already exists;	not overwritten
~~~

