<h1><center>TCGA_BreastCancer_RPPA</center></h1>
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

&#10060;	Row 9 of "test_data.tsv" should contain exactly three columns.

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (9; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	14-3-3_beta-R-V	|	14-3-3_epsilon-M-C	|	14-3-3_zeta-R-V	|	4E-BP1-R-V	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-A7-A4SD-01	|	-0.1118674675	|	0.0557315650000003	|	-0.2758670465	|	0.405752353	|
|	TCGA-E2-A15A-06	|	-0.22705919575	|	-0.14114607775	|	0.16453064175	|	0.0347185742499999	|
|	TCGA-OL-A66K-01	|	0.442160763	|	0.1245134725	|	-0.345147712	|	-0.2655260375	|
|	TCGA-AQ-A54O-01	|	-0.0532260532500002	|	0.10641983825	|	0.42880721875	|	0.56220893625	|

**Columns: 282 Rows: 938**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 9 of "test_data.tsv" does not contain 3 columns

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#10060;	Row: 3 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	TCGA-E2-A15A-06	|	14-3-3_beta-R-V	|		|
|	**User Generated**	|	TCGA-E2-A15A-06	|	14-3-3_beta-R-V	|	-0.22705919575	|

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#10060;	Row: 9 - Sample "" is not found in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
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

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "TCGA-BH-A1FN-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A18L-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-A7-A4SE-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-BH-A0DK-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-E9-A1RD-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-E9-A1N8-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-AC-A5EI-01" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-E9-A1RC-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "TCGA-E9-A1N5-11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 8325</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
