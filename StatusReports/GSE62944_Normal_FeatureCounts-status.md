<h1><center>GSE62944_Normal_FeatureCounts</center></h1>
<h2><center> Status: Complete </center></h2>
<center>Mar 05, 18. 13:03 MST</center>


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

|	Sample	|	1/2-SBSRNA4	|	A1BG	|	A1BG-AS1	|	A1CF	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-06-0675-11A-32R-A36H-07	|	48	|	206	|	87	|	8	|
|	TCGA-06-0678-11A-32R-A36H-07	|	25	|	112	|	44	|	2	|
|	TCGA-06-0680-11A-32R-A36H-07	|	36	|	223	|	122	|	5	|
|	TCGA-06-0681-11A-41R-A36H-07	|	28	|	361	|	120	|	1	|

**Columns: 23369 Rows: 742**

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
|	TCGA-06-0675-11A-32R-A36H-07	|	Cancer_Type	|	Glioblastoma multiforme	|
|	TCGA-06-0678-11A-32R-A36H-07	|	Cancer_Type	|	Glioblastoma multiforme	|
|	TCGA-06-0680-11A-32R-A36H-07	|	Cancer_Type	|	Glioblastoma multiforme	|
|	TCGA-06-0681-11A-41R-A36H-07	|	Cancer_Type	|	Glioblastoma multiforme	|

**Columns: 3 Rows: 742**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

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
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
