<h1><center>BiomarkerBenchmark_GSE5462</center></h1>
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
|	GSM125127	|	0.851553278823529	|	0.2227382275	|	1.45640476111111	|	0.407663862608696	|
|	GSM125129	|	0.641224656470588	|	-0.27550820625	|	1.53331146777778	|	0.571383662608696	|
|	GSM125131	|	0.647620414117647	|	-0.25349401625	|	1.35111683888889	|	0.345635635217391	|
|	GSM125133	|	0.938779574117647	|	-0.27325422375	|	1.22325687444444	|	0.434253175217391	|

**Columns: 11833 Rows: 48**

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
|	GSM125127	|	ID	|	12A	|
|	GSM125127	|	Treatment_Status	|	pretreatment	|
|	GSM125127	|	Treatment_Response	|	responder	|
|	GSM125129	|	ID	|	13A	|

**Columns: 3 Rows: 142**

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
