<h1><center>LINCS_PhaseI_Level5</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Feb 07, 18 23:02PM MST</center>


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

&#10060;	Row 29 of "test_metadata.tsv" should contain exactly three columns.

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (40; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	PSME1	|	ATF1	|	RHEB	|	FOXO3	|
|	---	|	---	|	---	|	---	|	---	|
|	CPC005_A375_6H:BRD-A85280935-003-01-7:10	|	0.773768961429596	|	-0.8184680342674255	|	0.1895722895860672	|	-0.14603076875209808	|
|	CPC005_A375_6H:BRD-A07824748-001-02-6:10	|	-0.6455861330032349	|	-0.8107486963272095	|	0.4590602517127991	|	-0.2246764600276947	|
|	CPC004_A375_6H:BRD-K20482099-001-01-1:10	|	-5.449665546417236	|	2.39377498626709	|	1.279789924621582	|	2.16786789894104	|
|	CPC005_A375_6H:BRD-K62929068-001-03-3:10	|	0.19340771436691284	|	-0.5822432637214661	|	-0.17897698283195496	|	-1.182024598121643	|

**Columns: 12329 Rows: 473648**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row: 1 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	AML001_CD34_24H:A05	|	PSME1	|	0.577400028706	|
|	**User Generated**	|	AML001_CD34_24H:A05	|	PSME1	|	0.5774000287055969	|

&#10060;	Row: 2 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	AML001_CD34_24H:A05	|	ACTB	|	0.421900004148	|
|	**User Generated**	|	AML001_CD34_24H:A05	|	ACTB	|	0.4219000041484833	|

&#10060;	Row: 3 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	TAK004_U2OS_96H:TRCN0000381509:1	|	PSME1	|	0.421341598034	|
|	**User Generated**	|	TAK004_U2OS_96H:TRCN0000381509:1	|	PSME1	|	0.42134159803390503	|

&#10060;	Row: 4 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	TAK004_U2OS_96H:TRCN0000381509:1	|	ACTB	|	-0.168426394463	|
|	**User Generated**	|	TAK004_U2OS_96H:TRCN0000381509:1	|	ACTB	|	-0.16842639446258545	|

&#10060;	Row: 5 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	AML001_CD34_24H:BRD-A03772856:10	|	PSME1	|	0.365400016308	|
|	**User Generated**	|	AML001_CD34_24H:BRD-A03772856:10	|	PSME1	|	0.3654000163078308	|

&#10060;	Row: 6 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	AML001_CD34_24H:BRD-A03772856:10	|	ACTB	|	-0.487500011921	|
|	**User Generated**	|	AML001_CD34_24H:BRD-A03772856:10	|	ACTB	|	-0.48750001192092896	|

&#10060;	Row: 7 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	AML001_CD34_6H:A05	|	PSME1	|	-0.122400000691	|
|	**User Generated**	|	AML001_CD34_6H:A05	|	PSME1	|	-0.12240000069141388	|

&#10060;	Row: 8 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	AML001_CD34_6H:A05	|	ACTB	|	1.12240004539	|
|	**User Generated**	|	AML001_CD34_6H:A05	|	ACTB	|	1.1224000453948975	|

&#10060;	Row: 9 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	CPC009_PC3_6H:BRD-A05565054-001-01-7:10	|	PSME1	|	-2.7532787323	|
|	**User Generated**	|	CPC009_PC3_6H:BRD-A05565054-001-01-7:10	|	PSME1	|	-2.7532787322998047	|

&#10060;	Row: 10 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	CPC009_PC3_6H:BRD-A05565054-001-01-7:10	|	ACTB	|	0.471796810627	|
|	**User Generated**	|	CPC009_PC3_6H:BRD-A05565054-001-01-7:10	|	ACTB	|	0.47179681062698364	|

&#10060;	Row: 11 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	CPC009_PC3_6H:A17	|	PSME1	|	-0.00356706418097	|
|	**User Generated**	|	CPC009_PC3_6H:A17	|	PSME1	|	-0.003567064180970192	|

&#10060;	Row: 12 - FAIL

||	Sample	|	Column	|	Row	|
|	---	|	---	|	---	|	---	|
|	**Expected**	|	CPC009_PC3_6H:A17	|	ACTB	|	-0.693475604057	|
|	**User Generated**	|	CPC009_PC3_6H:A17	|	ACTB	|	-0.693475604057312	|

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	AML001_CD34_24H:A05	|	pert_id	|	DMSO	|
|	AML001_CD34_24H:A05	|	distil_cc_q75	|	-666.0	|
|	AML001_CD34_24H:A05	|	distil_ss	|	4.78894	|
|	AML001_CD34_24H:A05	|	ngenes_modulated_up_lm	|	35	|

**Columns: 3 Rows: 11855982**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "donor_ethnicity" for all samples is the same ("Caucasian"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#10060;	Row 5: Fail
- "AML001_CD34_24H:A05	pert_itime	24 h" is not found.

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#10060;	Row 11: Fail
- "AML001_CD34_24H:A05	subtype	suspension" is not found.

&#9989;	Row 12: Success

&#9989;	Row 13: Success

&#9989;	Row 14: Success

&#9989;	Row 15: Success

&#10060;	Row 16: Fail
- "AML001_CD34_24H:A06	pert_itime	24 h" is not found.

&#9989;	Row 17: Success

&#9989;	Row 18: Success

&#9989;	Row 19: Success

&#9989;	Row 20: Success

&#9989;	Row 21: Success

&#10060;	Row 22: Fail
- "AML001_CD34_24H:A06	subtype	suspension" is not found.

&#9989;	Row 23: Success

&#9989;	Row 24: Success

&#9989;	Row 25: Success

&#9989;	Row 26: Success

&#10060;	Row 27: Fail
- "TAK004_U2OS_96H:TRCN0000370751:1	pert_itime	96 h" is not found.

&#10060;	Row 28: Fail
- "TAK004_U2OS_96H:TRCN0000370751:1	is_touchstone	0" is not found.

&#10060;	Row 29: Fail
- "TAK004_U2OS_96H:TRCN0000370751:1	tas_q75		0.288657" is not found.

&#9989;	Row 30: Success

&#9989;	Row 31: Success

&#9989;	Row 32: Success

&#9989;	Row 33: Success

&#9989;	Row 34: Success

&#9989;	Row 35: Success

&#10060;	Row 36: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	pert_itime	96 h" is not found.

&#10060;	Row 37: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	is_touchstone	0" is not found.

&#10060;	Row 38: Fail
- "TAK004_U2OS_96H:TRCN0000381509:1	tas_q75	0.169385" is not found.

&#9989;	Row 39: Success

&#9989;	Row 40: Success

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
