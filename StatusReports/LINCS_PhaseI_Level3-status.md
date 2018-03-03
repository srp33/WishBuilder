<h1><center>LINCS_PhaseI_Level3</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 03, 18 07:03AM MST</center>


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

&#9989;	test_metadata.tsv contains enough test cases (39; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	PSME1	|	ATF1	|	RHEB	|	FOXO3	|
|	---	|	---	|	---	|	---	|	---	|
|	CPC005_A375_6H_X1_B3_DUO52HI53LO:K06	|	11.0495004654	|	8.16800022125	|	12.7961997986	|	5.45459985733	|
|	CPC005_A375_6H_X2_B3_DUO52HI53LO:K06	|	10.6127996445	|	7.78684997559	|	12.0471000671	|	6.32849979401	|
|	CPC005_A375_6H_X3_B3_DUO52HI53LO:K06	|	10.6833000183	|	7.74604988098	|	12.3447999954	|	6.06804990768	|
|	CPC005_A375_6H_X1_B3_DUO52HI53LO:C19	|	10.6188001633	|	8.22739982605	|	12.7084999084	|	5.39309978485	|

**Columns: 12329 Rows: 1319139**

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
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	rna_plate	|	ASG001_MCF7_24H_X1	|
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	rna_well	|	F13	|
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	pert_id	|	DMSO	|
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	pert_iname	|	DMSO	|

**Columns: 3 Rows: 23138458**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "donor_ethnicity" for all samples is the same ("Caucasian"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#10060;	Row 3: Fail
- "ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	is_touchstone	1" is not found.

&#10060;	Row 4: Fail
- "ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	canonical_smiles	CS(=O)C" is not found.

&#10060;	Row 5: Fail
- "ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	tas_q75	0.122766" is not found.

&#10060;	Row 6: Fail
- "ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	icc	0.313591927289963" is not found.

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

&#10060;	Row 13: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	is_touchstone	0" is not found.

&#10060;	Row 14: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	canonical_smiles	COCC1OC(=O)c2coc3c2C1(C)C1=C(C2CCC(=O)C2(C)CC1OC(C)=O)C3=O" is not found.

&#10060;	Row 15: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	tas_q75	0.41063425" is not found.

&#10060;	Row 16: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	icc	0.478662326931953" is not found.

&#9989;	Row 17: Success

&#9989;	Row 18: Success

&#9989;	Row 19: Success

&#9989;	Row 20: Success

&#9989;	Row 21: Success

&#9989;	Row 22: Success

&#10060;	Row 23: Fail
- "KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04	is_touchstone	1" is not found.

&#10060;	Row 24: Fail
- "KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04	tas_q75	0.3074425" is not found.

&#10060;	Row 25: Fail
- "KDB001_MCF7_144H_X3_B1_DUO53HI52LO:D04	icc	0.682715356349945" is not found.

&#9989;	Row 26: Success

&#9989;	Row 27: Success

&#9989;	Row 28: Success

&#9989;	Row 29: Success

&#9989;	Row 30: Success

&#9989;	Row 31: Success

&#10060;	Row 32: Fail
- "CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23	is_touchstone	1" is not found.

&#10060;	Row 33: Fail
- "CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23	pubchem_cid	4452" is not found.

&#10060;	Row 34: Fail
- "CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23	tas_q75	0.219453" is not found.

&#10060;	Row 35: Fail
- "CPC001_VCAP_6H_X5_B5_DUO52HI53LO:M23	icc	0.394875109195709" is not found.

&#9989;	Row 36: Success

&#9989;	Row 37: Success

&#9989;	Row 38: Success

&#9989;	Row 39: Success

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
