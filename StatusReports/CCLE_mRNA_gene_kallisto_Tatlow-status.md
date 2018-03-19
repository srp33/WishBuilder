<h1><center>CCLE_mRNA_gene_kallisto_Tatlow</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 19, 18 10:03AM MST</center>


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

Executing download.sh: Success

Executing parse.sh: 

&#10060;	parse.sh returned an error:
~~~bash
Traceback (most recent call last):
  File "parse.py", line 13, in <module>
    with open(drugData, 'r') as f :
FileNotFoundError: [Errno 2] No such file or directory: 'tmp/CCLE_NP24.2009_Drug_data_2015.02.24.csv'
gzip: metadata.tsv: No such file or directory
gzip: data.tsv: No such file or directory
~~~

