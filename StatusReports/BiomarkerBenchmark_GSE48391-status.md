<h1><center>BiomarkerBenchmark_GSE48391</center></h1>
## Status: Complete
### Testing Directory . . .

#### Results: PASS
---
### Testing file paths:

&#9989;	test_data.tsv exists.

&#9989;	test_metadata.tsv exists.

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

*Running user code . . .*

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

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM1176873	|	1.91520238647059	|	-0.16594937375	|	2.24332934111111	|	0.6456344653125	|
|	GSM1176874	|	1.72492498882353	|	0.15464380125	|	2.44425712888889	|	1.041714703125	|
|	GSM1176875	|	2.37773027823529	|	-0.06224144375	|	2.22799032	|	1.0387700146875	|
|	GSM1176876	|	1.75267963647059	|	1.54216853125	|	2.24856010333333	|	0.55236123625	|

**Columns: 20025 Rows: 81**

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
|	GSM1176873	|	er	|	positive	|
|	GSM1176873	|	event	|	disease-free	|
|	GSM1176873	|	her2	|	normal	|
|	GSM1176873	|	hu306_classification	|	Luminal A	|

**Columns: 3 Rows: 561**

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

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
