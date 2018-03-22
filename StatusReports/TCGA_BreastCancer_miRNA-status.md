<h1><center>TCGA_BreastCancer_miRNA</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 22, 18 16:03PM MST</center>


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

&#10060;	Row 17 of "test_metadata.tsv" should contain exactly three columns.

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (17; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	MIMAT0019868	|	MIMAT0019869	|	MIMAT0019860	|	MIMAT0019862	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-OL-A66H-01	|	0.2381	|	NA	|	NA	|	NA	|
|	TCGA-3C-AALK-01	|	NA	|	0.2117	|	NA	|	NA	|
|	TCGA-AR-A1AH-01	|	NA	|	NA	|	NA	|	NA	|
|	TCGA-AC-A5EH-01	|	NA	|	NA	|	NA	|	NA	|

**Columns: 2239 Rows: 833**

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
- "TCGA-3C-AAAU-01	form_completion_date	2014-1-13" is not found.

&#10060;	Row 2: Fail
- "TCGA-3C-AAAU-01	metastatic_tumor_indicator	[Not Available]" is not found.

&#10060;	Row 3: Fail
- "TCGA-3C-AAAU-01	Somatic mutation	SRBD1" is not found.

&#10060;	Row 4: Fail
- "TCGA-3C-AAAU-01	Somatic mutation	PTCHD1" is not found.

&#10060;	Row 5: Fail
- "TCGA-3C-AALI-01	form_completion_date	2014-7-28" is not found.

&#10060;	Row 6: Fail
- "TCGA-3C-AALI-01	metastatic_tumor_indicator	[Not Available]" is not found.

&#10060;	Row 7: Fail
- "TCGA-3C-AALI-01	Somatic mutation	ADRA2C" is not found.

&#10060;	Row 8: Fail
- "TCGA-3C-AALI-01	Somatic mutation	NUDT10" is not found.

&#10060;	Row 9: Fail
- "TCGA-Z7-A8R5-01	form_completion_date	2014-7-9" is not found.

&#10060;	Row 10: Fail
- "TCGA-Z7-A8R5-01	metastatic_tumor_indicator	[Not Available]" is not found.

&#10060;	Row 11: Fail
- "TCGA-Z7-A8R5-01	Somatic mutation	DHX9" is not found.

&#10060;	Row 12: Fail
- "TCGA-Z7-A8R5-01	Somatic mutation	DYNC1I1" is not found.

&#10060;	Row 13: Fail
- "TCGA-Z7-A8R6-01	form_completion_date	2014-7-9" is not found.

&#10060;	Row 14: Fail
- "TCGA-Z7-A8R6-01	metastatic_tumor_indicator	[Not Available]" is not found.

&#10060;	Row 15: Fail
- "TCGA-Z7-A8R6-01	Somatic mutation	PRMT6" is not found.

&#10060;	Row 16: Fail
- "TCGA-Z7-A8R6-01	Somatic mutation	STAG2" is not found.

&#10060;	Row 17: Fail
- "" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "TCGA-BH-A1FJ-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A18S-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A0H5-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A13E-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A208-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A1EN-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-E2-A1L7-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A0HA-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A1FD-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 8490</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
