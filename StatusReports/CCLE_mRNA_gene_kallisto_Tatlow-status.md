<h1><center>CCLE_mRNA_gene_kallisto_Tatlow</center></h1>
<h2><center> Status: In Progress </center></h2>

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

Executing parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Key Files:

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#10060;	"22RV1_PROSTATE" does not have enough features to test (min: 2)

&#10060;	"OUMS27_BONE" does not have enough features to test (min: 2)

&#10060;	"RH18_SOFT_TISSUE\" does not have enough features to test (min: 2)

&#10060;	"RH18_SOFT_TISSUE" does not have enough features to test (min: 2)

&#9989;	test_metadata.tsv contains enough test cases (28; min: 8)

#### Results: **<font color="red">FAIL</font>**
---
