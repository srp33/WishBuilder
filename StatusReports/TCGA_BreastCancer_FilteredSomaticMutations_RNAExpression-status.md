<h1><center>TCGA_BreastCancer_FilteredSomaticMutations_RNAExpression</center></h1>
<h2><center> Status: In Progress </center></h2>

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

Executing parse.sh: Success

&#10060;	data.tsv.gzexists, but was not zipped correctly.

&#10060;	metadata.tsv.gzexists, but was not zipped correctly.

#### Results: **<font color="red">FAIL</font>**
---
