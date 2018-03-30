<h1><center>CCLE_mRNA_gene_kallisto_Tatlow</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 30, 18 14:03PM MST</center>


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

&#9989;	test_metadata.tsv contains enough test cases (28; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ARF5	|	M6PR	|	ESRRA	|	FKBP4	|
|	---	|	---	|	---	|	---	|	---	|
|	CORL24_LUNG	|	185.74321500000002	|	102.68621531890001	|	18.638011	|	114.56292900000001	|
|	HSC3_UPPER_AERODIGESTIVE_TRACT	|	111.76097300000002	|	137.56579900000003	|	33.803128	|	90.439629	|
|	KMS11_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE	|	137.16564	|	120.71723099999998	|	23.442102999999996	|	168.42325000000002	|
|	C2BBE1_LARGE_INTESTINE	|	230.49874299999996	|	211.75282130402402	|	35.42388900000001	|	142.86827899999997	|

**Columns: 58685 Rows: 923**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row: 1 - Sample "COR-L24" is not found in data.tsv.gz

&#10060;	Row: 2 - Sample "COR-L24" is not found in data.tsv.gz

&#10060;	Row: 3 - Sample "HSC-3" is not found in data.tsv.gz

&#10060;	Row: 4 - Sample "HSC-3" is not found in data.tsv.gz

&#10060;	Row: 5 - Sample "HT55" is not found in data.tsv.gz

&#10060;	Row: 6 - Sample "HT55" is not found in data.tsv.gz

&#10060;	Row: 7 - Sample "COLO-680N" is not found in data.tsv.gz

&#10060;	Row: 8 - Sample "COLO-680N" is not found in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	CORL24_LUNG	|	Gender	|	M	|
|	CORL24_LUNG	|	Site Primary	|	lung	|
|	CORL24_LUNG	|	Histology	|	carcinoma	|
|	CORL24_LUNG	|	Hist Subtype1	|	small_cell_carcinoma	|

**Columns: 3 Rows: 212420**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Oncomap" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Hybrid Capture Sequencing" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

&#10060;	Row 1: Fail
- "COR-L24	Gender	M" is not found.

&#10060;	Row 2: Fail
- "COR-L24	Hybrid Capture Sequencing	yes" is not found.

&#10060;	Row 3: Fail
- "KMS-11	Drug__AEW541__EC50 (uM)	0.236332193" is not found.

&#10060;	Row 4: Fail
- "KMS-11	Drug__AEW541__ActArea	3.2272" is not found.

&#10060;	Row 5: Fail
- "KMS-11	Drug__Erlotinib__IC50 (uM)	8" is not found.

&#10060;	Row 6: Fail
- "KMS-11	Drug__Erlotinib__ActArea	0.2748" is not found.

&#10060;	Row 7: Fail
- "KMS-11	Drug__Tarceva__IC50 (uM)	8" is not found.

&#10060;	Row 8: Fail
- "KMS-11	Drug__Tarceva__ActArea	0.2748" is not found.

&#10060;	Row 9: Fail
- "HT-144	Drug__AEW541__EC50 (uM)	3.215185642" is not found.

&#10060;	Row 10: Fail
- "HT-144	Drug__AEW541__ActArea	0.8903" is not found.

&#10060;	Row 11: Fail
- "HT-144	Drug__Erlotinib__EC50 (uM)	9.204066346" is not found.

&#10060;	Row 12: Fail
- "HT-144	Drug__Erlotinib__ActArea	0.5338" is not found.

&#10060;	Row 13: Fail
- "HT-144	Drug__Tarceva__EC50 (uM)	9.204066346" is not found.

&#10060;	Row 14: Fail
- "HT-144	Drug__Tarceva__ActArea	0.5338" is not found.

&#10060;	Row 15: Fail
- "HSC-3	Gender	M" is not found.

&#10060;	Row 16: Fail
- "HSC-3	Hybrid Capture Sequencing	yes" is not found.

&#10060;	Row 17: Fail
- "HT55	Site Primary	large_intestine" is not found.

&#10060;	Row 18: Fail
- "HT55	Hybrid Capture Sequencing	yes" is not found.

&#10060;	Row 19: Fail
- "COLO-680N	Gender	F" is not found.

&#10060;	Row 20: Fail
- "COLO-680N	Hybrid Capture Sequencing	yes" is not found.

&#9989;	Row 21: Success

&#9989;	Row 22: Success

&#9989;	Row 23: Success

&#10060;	Row 24: Fail
- "OUMS27_BONE	SomaticMutation	FMN2" is not found.

&#10060;	Row 25: Fail
- "LOUNH91_LUNG	CNV__A1BG	-0.0259" is not found.

&#10060;	Row 26: Fail
- "LOUNH91_LUNG	CNV__SCO2	-0.103" is not found.

&#10060;	Row 27: Fail
- "RH18_SOFT_TISSUE	CNV__A1BG	-0.0433" is not found.

&#10060;	Row 28: Fail
- "RH18_SOFT_TISSUE	CNV__SCO2	-0.3008" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "MS1_LUNG" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "CP66EBV_MATCHED_NORMAL_TISSUE" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "INA6_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "D336MG_CENTRAL_NERVOUS_SYSTEM" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "MLMA_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "SW156_KIDNEY" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "ES4_BONE" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "HS751T_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "ARH77_HAEMATOPOIETIC_AND_LYMPHOID_TISSUE" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 575</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
