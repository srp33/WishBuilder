## Status: Complete
##### Testing Directory . . .

###### Results: PASS
---
##### Testing file paths:

&#9989;	test_data.tsv exists.

&#9989;	test_metadata.tsv exists.

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

**Running user code . . .**

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

###### Results: PASS
---
##### Testing Key Files:

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

###### Results: PASS
---

##### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENST00000000233.9	|	ENST00000000412.7	|	ENST00000000442.10	|	ENST00000001008.5	|
|	---	|	---	|	---	|	---	|	---	|
|	COR-L24	|	119.261	|	53.0379	|	6.99391	|	77.702	|
|	HSC-3	|	86.1598	|	106.027	|	13.0669	|	67.9185	|
|	KMS-11	|	101.817	|	79.8547	|	5.65856	|	116.169	|
|	C2BBe1	|	149.497	|	155.488	|	9.85457	|	110.965	|

**Columns: 199170 Rows: 923**

---
### data.tsv.gz Test Cases . . .

&#9989;	First column of file is titled "Sample"

&#9989;	Test 1: Success

&#9989;	Test 2: Success

&#9989;	Test 3: Success

&#9989;	Test 4: Success

&#9989;	Test 5: Success

&#9989;	Test 6: Success

&#9989;	Test 7: Success

&#9989;	Test 8: Success

##### Results: PASS
---
##### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	COR-L24	|	Gender	|	M	|
|	COR-L24	|	Site Primary	|	lung	|
|	COR-L24	|	Histology	|	carcinoma	|
|	COR-L24	|	Hist Subtype1	|	small_cell_carcinoma	|

**Columns: 3 Rows: 8330**

---
### metadata.tsv.gz Test Cases . . .

&#9989;	First column of file is titled "Sample"

&#9989;	Test 1: Success

&#9989;	Test 2: Success

&#9989;	Test 3: Success

&#9989;	Test 4: Success

&#9989;	Test 5: Success

&#9989;	Test 6: Success

&#9989;	Test 7: Success

&#9989;	Test 8: Success

##### Results: PASS
---
##### Comparing samples in both files . . .

###### Results: PASS

---
##### Testing Directory after cleanup . . .

###### Results: PASS
---
