<h1><center>CCLE_mRNA_gene_kallisto_Tatlow</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 22, 18 16:03PM MST</center>


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

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (20; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ARF5	|	M6PR	|	ESRRA	|	FKBP4	|
|	---	|	---	|	---	|	---	|	---	|
|	CORL24_LUNG	|	185.74321500000002	|	102.68621531890001	|	18.638011	|	114.56292900000001	|
|	HSC3_UPPER_AERODIGESTIVE_TRACT	|	111.76097300000002	|	137.56579900000003	|	33.803128	|	90.439629	|
|	KMS11_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE	|	137.16564	|	120.71723099999998	|	23.442102999999996	|	168.42325000000002	|
|	C2BBE1_LARGE_INTESTINE	|	230.49874299999996	|	211.75282130402402	|	35.42388900000001	|	142.86827899999997	|

**Columns: 58685 Rows: 923**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#10060;	Row: 9 - CNV__A1BG is not found in "data.tsv.gz" column headers

&#10060;	Row: 10 - CNV__SCO2 is not found in "data.tsv.gz" column headers

&#10060;	Row: 11 - CNV__A1BG is not found in "data.tsv.gz" column headers

&#10060;	Row: 12 - CNV__SCO2 is not found in "data.tsv.gz" column headers

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	CORL24_LUNG	|	Gender	|	M	|
|	CORL24_LUNG	|	Site Primary	|	lung	|
|	CORL24_LUNG	|	Histology	|	carcinoma	|
|	CORL24_LUNG	|	Hist Subtype1	|	small_cell_carcinoma	|

**Columns: 3 Rows: 67350**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Oncomap" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Hybrid Capture Sequencing" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

&#9989;	Row 13: Success

&#9989;	Row 14: Success

&#9989;	Row 15: Success

&#9989;	Row 16: Success

&#9989;	Row 17: Success

&#9989;	Row 18: Success

&#9989;	Row 19: Success

&#9989;	Row 20: Success

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
