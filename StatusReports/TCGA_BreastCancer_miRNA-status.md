<h1><center>TCGA_BreastCancer_miRNA</center></h1>
<h2><center> Status: Complete </center></h2>
<center>Apr 10, 18. 15:04 MST</center>


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

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	MIMAT0019868	|	MIMAT0019869	|	MIMAT0019860	|	MIMAT0019862	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-OL-A66H-01	|	0.2381	|	NA	|	NA	|	NA	|
|	TCGA-3C-AALK-01	|	NA	|	0.2117	|	NA	|	NA	|
|	TCGA-AR-A1AH-01	|	NA	|	NA	|	NA	|	NA	|
|	TCGA-AC-A5EH-01	|	NA	|	NA	|	NA	|	NA	|

**Columns: 2239 Rows: 755**

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

#### Results: PASS
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	TCGA-A7-A3J0-01	|	Somatic mutation	|	BRCA	|
|	TCGA-E2-A14X-01	|	Somatic mutation	|	BRCA	|
|	TCGA-A7-A13G-01	|	Somatic mutation	|	BRCA	|
|	TCGA-E2-A15S-01	|	Somatic mutation	|	BRCA	|

**Columns: 3 Rows: 769**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Somatic mutation" for all samples is the same ("BRCA"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
