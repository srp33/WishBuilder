<h1><center>ICGC_BRCA-US_exp_seq</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Jan 22, 18 17:01PM MST</center>


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

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Key Files:

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (9; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (9; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	A1BG	|	A1CF	|	A2BP1	|	A2LD1	|
|	---	|	---	|	---	|	---	|	---	|
|	DO1249	|	644	|	0	|	0	|	144	|
|	DO1250	|	514	|	0	|	0	|	87	|
|	DO1251	|	541	|	0	|	4	|	451	|
|	DO1252	|	467	|	0	|	0	|	184	|

**Columns: 20502 Rows: 1042**

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

&#9989;	Row 9: Success

#### Results: PASS
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	DO1808	|	TCGA_ID	|	TCGA-E2-A15C	|
|	DO1808	|	disease_status_last_followup	|	complete remission	|
|	DO1808	|	vital_status	|	alive	|
|	DO1808	|	age_at_diagnosis	|	61	|

**Columns: 3 Rows: 8329**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#10060;	Row 4: Fail
- "DO219611	sex	female" is not found.

&#10060;	Row 5: Fail
- "DO219611	TCGA_ID	TCGA-BH-A6R9" is not found.

&#10060;	Row 6: Fail
- "DO219611	disease_status_last_followup	complete remission" is not found.

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
