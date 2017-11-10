<h1><center>GSE62944_Normal_FeatureCounts</center></h1>
<h2><center> Status: In Progress </center></h2>


### Testing Directory . . .

#### Results: PASS
---
### Testing Description File . . .

&#9989;	Title is less than 100 characters

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

|	SampleID	|	1/2-SBSRNA4	|	A1BG	|	A1BG-AS1	|	A1CF	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-06-0675-11A-32R-A36H-07	|	48	|	206	|	87	|	8	|
|	TCGA-06-0678-11A-32R-A36H-07	|	25	|	112	|	44	|	2	|
|	TCGA-06-0680-11A-32R-A36H-07	|	36	|	223	|	122	|	5	|
|	TCGA-06-0681-11A-41R-A36H-07	|	28	|	361	|	120	|	1	|

**Columns: 23369 Rows: 742**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	First column of file must be titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	SampleID	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	TCGA-06-0675-11A-32R-A36H-07	|	Cancer_Type	|	GBM	|
|	TCGA-06-0678-11A-32R-A36H-07	|	Cancer_Type	|	GBM	|
|	TCGA-06-0680-11A-32R-A36H-07	|	Cancer_Type	|	GBM	|
|	TCGA-06-0681-11A-41R-A36H-07	|	Cancer_Type	|	GBM	|

**Columns: 3 Rows: 742**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	First column of file must be titled "Sample"

&#10060;	Row 1: Fail
- "TCGA-K4-A3WV-11A-21R-A22U-07    Cancer_Type	BLCA" is not found.

&#10060;	Row 2: Fail
- "TCGA-49-6742-11A-01R-1858-07    Cancer_Type	LUAD" is not found.

&#10060;	Row 3: Fail
- "TCGA-DD-A3A2-11A-11R-A213-07    Cancer_Type	LIHC" is not found.

&#10060;	Row 4: Fail
- "TCGA-BH-A0DV-11A-22R-A12P-07    Cancer_Type	BRCA" is not found.

&#10060;	Row 5: Fail
- "TCGA-GE-A2C6-11A-11R-A16R-07    Cancer_Type	THCA" is not found.

&#10060;	Row 6: Fail
- "TCGA-56-7730-11A-01R-2125-07    Cancer_Type	LUSC" is not found.

&#10060;	Row 7: Fail
- "TCGA-BH-A0H5-11A-62R-A115-07    Cancer_Type	BRCA" is not found.

&#10060;	Row 8: Fail
- "TCGA-22-5489-11A-01R-1635-07    Cancer_Type	LUSC" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

&#9989;	No Commas in metadata.tsv.gz

&#9989;	No Commas in data.tsv.gz

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
