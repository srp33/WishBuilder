##<center>##BiomarkerBenchmark_GSE30784</center>

### Testing Directory . . .
## Status: Complete

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
|	GSM764749	|	2.07598720058824	|	-0.20218943375	|	2.91173383222222	|	0.5654668003125	|
|	GSM764750	|	1.52020662176471	|	-0.2662692825	|	2.55659381222222	|	0.3702671903125	|
|	GSM764751	|	1.21595023764706	|	-0.27813332125	|	2.54325946222222	|	0.452511955	|
|	GSM764752	|	1.34750764352941	|	-0.2356730175	|	2.54195578111111	|	0.4074068203125	|

**Columns: 20025 Rows: 226**

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
|	GSM764749	|	age	|	40-49	|
|	GSM764749	|	Sex	|	F	|
|	GSM764749	|	status	|	cancer	|
|	GSM764750	|	age	|	40-49	|

**Columns: 3 Rows: 676**

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
