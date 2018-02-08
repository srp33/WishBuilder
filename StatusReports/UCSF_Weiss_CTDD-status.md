<h1><center>UCSF_Weiss_CTDD</center></h1>
<h2><center> Status: Complete </center></h2>
<center>Feb 08, 18. 11:02 MST</center>


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

&#9989;	test_data.tsv contains enough test cases (11; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (9; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	0610007C21Rik	|	0610007L01Rik	|	0610007P08Rik	|	0610007P14Rik	|
|	---	|	---	|	---	|	---	|	---	|
|	RU109_1355	|	9.1900	|	8.3670	|	6.2000	|	8.9890	|
|	RU109_1358	|	8.8340	|	8.5230	|	5.9945	|	9.3620	|
|	RU109_1359	|	9.1900	|	8.2750	|	5.9500	|	8.9350	|
|	RU109_1361	|	9.1380	|	8.3780	|	5.8920	|	8.8210	|

**Columns: 19341 Rows: 21**

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

&#9989;	Row 10: Success

&#9989;	Row 11: Success

#### Results: PASS
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	RU109_1355	|	Sex	|	M	|
|	RU109_1355	|	Germline Hras1 status	|	Hras1-/-	|
|	RU109_1355	|	Color	|	agouti (tan)	|
|	RU109_1358	|	Sex	|	M	|

**Columns: 3 Rows: 1201**

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

&#9989;	Row 9: Success

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
