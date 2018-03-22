<h1><center>TCGA_BreastCancer_CNV</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 22, 18 15:03PM MST</center>


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

&#10060;	Row 9 of "test_metadata.tsv" should contain exactly three columns.

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (9; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ACAP3	|	ACTRT2	|	AGRN	|	ANKRD65	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-3C-AAAU-01	|	0	|	0	|	0	|	0	|
|	TCGA-3C-AALI-01	|	-1	|	-1	|	-1	|	-1	|
|	TCGA-3C-AALJ-01	|	-1	|	-1	|	-1	|	-1	|
|	TCGA-3C-AALK-01	|	0	|	0	|	0	|	0	|

**Columns: 24777 Rows: 1081**

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
|	TCGA-G9-A9S0-01	|	Somatic mutation	|	PRAD	|
|	TCGA-E1-5318-01	|	Somatic mutation	|	LGG	|
|	TCGA-25-1625-01	|	Somatic mutation	|	OV	|
|	TCGA-A2-A0T1-01	|	Somatic mutation	|	BRCA	|

**Columns: 3 Rows: 9265**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 1: Fail
- "TCGA-3C-AAAU-01	Somatic mutation	SRBD1" is not found.

&#10060;	Row 2: Fail
- "TCGA-3C-AAAU-01	Somatic mutation	PTCHD1" is not found.

&#10060;	Row 3: Fail
- "TCGA-3C-AALI-01	Somatic mutation	ADRA2C" is not found.

&#10060;	Row 4: Fail
- "TCGA-3C-AALI-01	Somatic mutation	NUDT10" is not found.

&#10060;	Row 5: Fail
- "TCGA-Z7-A8R5-01	Somatic mutation	DHX9" is not found.

&#10060;	Row 6: Fail
- "TCGA-Z7-A8R5-01	Somatic mutation	DYNC1I1" is not found.

&#10060;	Row 7: Fail
- "TCGA-Z7-A8R6-01	Somatic mutation	PRMT6" is not found.

&#10060;	Row 8: Fail
- "TCGA-Z7-A8R6-01	Somatic mutation	STAG2" is not found.

&#10060;	Row 9: Fail
- "" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "TCGA-C8-A9FZ-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-AC-A5EI-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-AR-A0U1-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A3-3331-01" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "TCGA-66-2785-01" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "TCGA-D3-A5GN-06" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "TCGA-G3-A7M8-01" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "TCGA-DJ-A4UW-01" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "TCGA-MP-A4T4-01" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 8092</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
