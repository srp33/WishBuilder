<h1><center>LINCS_PhaseI_Level5</center></h1>
<h2><center> Status: In Progress </center></h2>


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

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (16; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	PSME1	|	ATF1	|	RHEB	|	FOXO3	|
|	---	|	---	|	---	|	---	|	---	|
|	CPC005_A375_6H:BRD-A85280935-003-01-7:10	|	0.77376896143	|	-0.818468034267	|	0.189572289586	|	-0.146030768752	|
|	CPC005_A375_6H:BRD-A07824748-001-02-6:10	|	-0.645586133003	|	-0.810748696327	|	0.459060251713	|	-0.224676460028	|
|	CPC004_A375_6H:BRD-K20482099-001-01-1:10	|	-5.44966554642	|	2.39377498627	|	1.27978992462	|	2.16786789894	|
|	CPC005_A375_6H:BRD-K62929068-001-03-3:10	|	0.193407714367	|	-0.582243263721	|	-0.178976982832	|	-1.18202459812	|

**Columns: 12329 Rows: 473648**

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

&#9989;	Row 12: Success

#### Results: PASS
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	AML001_CD34_24H:A05	|	pert_id	|	DMSO	|
|	AML001_CD34_24H:A05	|	pert_iname	|	DMSO	|
|	AML001_CD34_24H:A05	|	pert_type	|	ctl_vehicle	|
|	AML001_CD34_24H:A05	|	pert_iname	|	DMSO	|

**Columns: 3 Rows: 8249413**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "donor_ethnicity" for all samples is the same ("Caucasian"). This variable has been removed from metadata.tsv.gz</p>

&#10060;	Row 1: Fail
- "AML001_CD34_24H:A05	pert_itime	24 h" is not found.

&#9989;	Row 2: Success

&#10060;	Row 3: Fail
- "AML001_CD34_24H:A05	is_touchstone	1" is not found.

&#10060;	Row 4: Fail
- "AML001_CD34_24H:A05	canonical_smiles	CS(=O)C" is not found.

&#10060;	Row 5: Fail
- "AML001_CD34_24H:A05	tas_q75	0.122766" is not found.

&#10060;	Row 6: Fail
- "AML001_CD34_24H:A05	icc	0.313591927289963" is not found.

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#10060;	Row 10: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	pert_itime	96 h " is not found.

&#9989;	Row 11: Success

&#10060;	Row 12: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	is_touchstone	0" is not found.

&#10060;	Row 13: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	tas_q75	0.169385" is not found.

&#9989;	Row 14: Success

&#9989;	Row 15: Success

&#9989;	Row 16: Success

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
