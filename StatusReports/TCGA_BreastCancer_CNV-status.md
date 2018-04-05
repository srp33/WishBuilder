<h1><center>TCGA_BreastCancer_CNV</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Apr 05, 18 16:04PM MST</center>


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

|	Sample	|	ACAP3	|	ACTRT2	|	AGRN	|	ANKRD65	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-3C-AAAU-01	|	0	|	0	|	0	|	0	|
|	TCGA-3C-AALI-01	|	-1	|	-1	|	-1	|	-1	|
|	TCGA-3C-AALJ-01	|	-1	|	-1	|	-1	|	-1	|
|	TCGA-3C-AALK-01	|	0	|	0	|	0	|	0	|

**Columns: 24777 Rows: 1078**

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
|	TCGA-A2-A0T1-01	|	Somatic mutation	|	BRCA	|
|	TCGA-A7-A3J0-01	|	Somatic mutation	|	BRCA	|
|	TCGA-AO-A126-01	|	Somatic mutation	|	BRCA	|
|	TCGA-E2-A14X-01	|	Somatic mutation	|	BRCA	|

**Columns: 3 Rows: 1066**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Somatic mutation" for all samples is the same ("BRCA"). This variable has been removed from metadata.tsv.gz</p>

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

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "TCGA-AC-A3QQ-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-AC-A2QH-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A26F-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A26E-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A13E-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A0DB-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-AC-A3OD-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A13D-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A0DC-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 12</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
