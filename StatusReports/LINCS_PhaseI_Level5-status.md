<h1><center>LINCS_PhaseI_Level5</center></h1>
<h2><center> Status: In Progress </center></h2>


### Testing Directory . . .

#### Results: PASS
---
### Testing Description File . . .

&#9989;	Title is less than 100 characters

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
|	AML001_CD34_24H:BRD-A03772856:10	|	0.365400016308	|	0.693850040436	|	0.554350018501	|	-0.315799981356	|
|	AML001_CD34_24H:BRD-A03772856:3.33333	|	0.296950012445	|	-0.126849994063	|	-1.42920005322	|	-0.332000017166	|
|	AML001_CD34_24H:BRD-A03772856:1.11111	|	-1.16809999943	|	-0.548200011253	|	-0.0293999910355	|	0.570549964905	|
|	AML001_CD34_24H:BRD-A03772856:0.37037	|	0.462899982929	|	-0.0881000012159	|	-0.486000001431	|	-0.664200007915	|

**Columns: 12329 Rows: 94775**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#10060;	Row: 3 - Sample "TAK004_U2OS_96H:TRCN0000381509:1" is not found in data.tsv.gz

&#10060;	Row: 4 - Sample "TAK004_U2OS_96H:TRCN0000381509:1" is not found in data.tsv.gz

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	AML001_CD34_24H:A05	|	pert_id	|	DMSO	|
|	AML001_CD34_24H:A05	|	is_touchstone	|	1	|
|	AML001_CD34_24H:A05	|	inchi_key_prefix	|	IAZDPXIOMUYVGZ	|
|	AML001_CD34_24H:A05	|	inchi_key	|	IAZDPXIOMUYVGZ-UHFFFAOYSA-N	|

**Columns: 3 Rows: 2316880**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	The value for variable "pert_time_unit" for all samples is the same ("h").

&#10060;	The value for variable "donor_ethnicity" for all samples is the same ("Caucasian").

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#10060;	Row 10: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	pert_itime	96 h " is not found.

&#10060;	Row 11: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	pert_id	TRCN0000381509	" is not found.

&#10060;	Row 12: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	is_touchstone	0" is not found.

&#10060;	Row 13: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	tas_q75	0.169385" is not found.

&#10060;	Row 14: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	cell_id	U2OS" is not found.

&#10060;	Row 15: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	cell_type	cell line" is not found.

&#10060;	Row 16: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	donor_ethnicity	Caucasian" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

&#10060;	Comma(s) exist in "metadata.tsv.gz"

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
