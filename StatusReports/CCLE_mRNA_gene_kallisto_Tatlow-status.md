<h1><center>CCLE_mRNA_gene_kallisto_Tatlow</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 09, 18 16:03PM MST</center>


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

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#10060;	"22RV1_PROSTATE" does not have enough features to test (min: 2)

&#10060;	"OUMS27_BONE" does not have enough features to test (min: 2)

&#9989;	test_metadata.tsv contains enough test cases (24; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ARF5	|	M6PR	|	ESRRA	|	FKBP4	|
|	---	|	---	|	---	|	---	|	---	|
|	COR-L24	|	185.74321500000002	|	102.68621531890001	|	18.638011	|	114.56292900000001	|
|	HSC-3	|	111.76097300000002	|	137.56579900000003	|	33.803128	|	90.439629	|
|	KMS-11	|	137.16564	|	120.71723099999998	|	23.442102999999996	|	168.42325000000002	|
|	C2BBe1	|	230.49874299999996	|	211.75282130402402	|	35.42388900000001	|	142.86827899999997	|

**Columns: 58685 Rows: 24296195**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row: 1 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	COR-L24	|	ARF5	|	185.743215	|
|	**User Generated**	|	COR-L24	|	ARF5	|	185.74321500000002	|

&#9989;	Row 2: Success

&#10060;	Row: 3 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	HSC-3	|	ARF5	|	111.760973	|
|	**User Generated**	|	HSC-3	|	ARF5	|	111.76097300000002	|

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#10060;	Row: 7 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	COLO-680N	|	ARF5	|	110.45471	|
|	**User Generated**	|	COLO-680N	|	ARF5	|	110.45470999999999	|

&#9989;	Row 8: Success

&#10060;	Row: 9 - CNV__A1BG is not found in "data.tsv.gz" column headers

&#10060;	Row: 10 - CNV__SCO2 is not found in "data.tsv.gz" column headers

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	COR-L24	|	Gender	|	M	|
|	COR-L24	|	Site Primary	|	lung	|
|	COR-L24	|	Histology	|	carcinoma	|
|	COR-L24	|	Hist Subtype1	|	small_cell_carcinoma	|

**Columns: 3 Rows: 205952**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Oncomap" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Hybrid Capture Sequencing" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

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

&#9989;	Row 12: Success

&#9989;	Row 13: Success

&#9989;	Row 14: Success

&#9989;	Row 15: Success

&#9989;	Row 16: Success

&#9989;	Row 17: Success

&#9989;	Row 18: Success

&#9989;	Row 19: Success

&#9989;	Row 20: Success

&#9989;	Row 21: Success

&#9989;	Row 22: Success

&#9989;	Row 23: Success

&#10060;	Row 24: Fail
- "OUMS27_BONE	SomaticMutation	FMN2" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "TC32_BONE" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "KELLY_p_CCLE_AffySNP_Oct2012_01_GenomeWideSNP_6_B01_1217624_KMS18_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "HS618T_LUNG" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "KCIMOH1_PANCREAS" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "HNT34" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "YMB1_BREAST" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "HS616T_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "HS698T_LARGE_INTESTINE" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "SNB19_CENTRAL_NERVOUS_SYSTEM" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 551</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
