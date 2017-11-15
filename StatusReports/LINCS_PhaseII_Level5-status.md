<h1><center>LINCS_PhaseII_Level5</center></h1>
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

&#9989;	test_metadata.tsv contains enough test cases (45; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	DDR1	|	PAX8	|	GUCA1A	|	EPHB3	|
|	---	|	---	|	---	|	---	|	---	|
|	LJP005_A375_24H:A03	|	-0.154526472092	|	-1.16547966003	|	0.188776731491	|	-0.402407795191	|
|	LJP005_A375_24H:A04	|	0.113874211907	|	-0.88341575861	|	-0.366105437279	|	0.392237842083	|
|	LJP005_A375_24H:A05	|	-0.0382520332932	|	-0.18391340971	|	0.925739884377	|	0.0286308526993	|
|	LJP005_A375_24H:A06	|	0.466993302107	|	-0.584318578243	|	-0.301697105169	|	0.594861209393	|

**Columns: 12329 Rows: 23601**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row: 5 - Success

&#9989;	Row: 6 - Success

&#9989;	Row: 7 - Success

&#9989;	Row: 8 - Success

&#9989;	Row: 1 - Success

&#9989;	Row: 2 - Success

&#9989;	Row: 9 - Success

&#9989;	Row: 10 - Success

&#9989;	Row: 11 - Success

&#9989;	Row: 12 - Success

&#9989;	Row: 3 - Success

&#10060;	Row: 4 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	LJP005_HA1E_24H:M01	|	ACTB	|	0.598744034767	|
|	**User Generated**	|	LJP005_HA1E_24H:M01	|	ACTB	|	-0.522399544716	|

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	LJP005_A375_24H:A03	|	pert_id	|	DMSO	|
|	LJP005_A375_24H:A03	|	distil_cc_q75	|	0.37	|
|	LJP005_A375_24H:A03	|	distil_ss	|	2.45357	|
|	LJP005_A375_24H:A03	|	tas	|	0.150663	|

**Columns: 3 Rows: 575205**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	All values for variable "precursor_cell_id" are the same("NPC").

&#10060;	All values for variable "donor_ethnicity" are the same("Caucasian").

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

&#9989;	Row 24: Success

&#9989;	Row 25: Success

&#9989;	Row 26: Success

&#9989;	Row 27: Success

&#9989;	Row 28: Success

&#9989;	Row 29: Success

&#9989;	Row 30: Success

&#9989;	Row 31: Success

&#9989;	Row 32: Success

&#9989;	Row 33: Success

&#9989;	Row 34: Success

&#9989;	Row 35: Success

&#10060;	Row 36: Fail
- "XPR002_YAPC.311_96H:N12	pert_id	BRDN0000735469" is not found.

&#10060;	Row 37: Fail
- "XPR002_YAPC.311_96H:N12	pert_iname	ACLY" is not found.

&#10060;	Row 38: Fail
- "XPR002_YAPC.311_96H:N12	cell_id	YAPC.311" is not found.

&#10060;	Row 39: Fail
- "XPR002_YAPC.311_96H:N12	pert_itime	96 h" is not found.

&#10060;	Row 40: Fail
- "XPR002_YAPC.311_96H:N12	distil_cc_q75	0.29" is not found.

&#10060;	Row 41: Fail
- "XPR002_YAPC.311_96H:N12	distil_nsample	3.04514" is not found.

&#10060;	Row 42: Fail
- "XPR002_YAPC.311_96H:N12	tas	0.137759" is not found.

&#10060;	Row 43: Fail
- "XPR002_YAPC.311_96H:N12	distil_nsample	2" is not found.

&#10060;	Row 44: Fail
- "XPR002_YAPC.311_96H:N12	cell_type	cell line" is not found.

&#10060;	Row 45: Fail
- "XPR002_YAPC.311_96H:N12	donor_sex	M" is not found.

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
