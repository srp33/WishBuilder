<h1><center>BiomarkerBenchmark_GSE2109_Uterus</center></h1>
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

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM46896	|	2.45170614941176	|	-0.26278781875	|	2.36851443	|	0.65793820125	|
|	GSM46914	|	2.34857037235294	|	-0.22124563	|	2.41402934	|	0.6655595775	|
|	GSM53050	|	0.997836810588235	|	-0.16768143125	|	2.39979773777778	|	0.3119599425	|
|	GSM53120	|	1.26050790588235	|	-0.1928293575	|	2.07793508444444	|	0.5244972803125	|

**Columns: 20025 Rows: 113**

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
|	GSM46896	|	Alcohol_Consumption	|	No	|
|	GSM46896	|	Days_from_Patient_Diagnosis_to_Excision	|	15	|
|	GSM46896	|	Ethnic_Background	|	Caucasian	|
|	GSM46896	|	Family_History_of_Cancer	|	Yes	|

**Columns: 3 Rows: 1725**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	The value for variable "Clinical_M" for all samples is the same ("0").

&#10060;	The value for variable "Relapse_Since_Primary_Treatment" for all samples is the same ("No").

&#10060;	The value for variable "Type_of_Tobacco_Use" for all samples is the same ("Cigarettes").

&#10060;	The value for variable "Grade" for all samples is the same ("3").

&#10060;	The value for variable "Have_you_ever_been_diagnosed_as_having_HPV_on_your_PAP_smear" for all samples is the same ("No").

&#10060;	The value for variable "Clinical_Multiple_Tumors" for all samples is the same ("No").

&#10060;	The value for variable "Primary_Site" for all samples is the same ("Endometrium").

&#10060;	The value for variable "Clinical_Stage_During_or_Following_Multimodality_Therapy" for all samples is the same ("No").

&#10060;	The value for variable "Ethnic_Background" for all samples is the same ("Caucasian").

&#10060;	The value for variable "Clinical_N" for all samples is the same ("0").

&#10060;	The value for variable "Stage" for all samples is the same ("No AJCC Scheme for this site and histology").

&#10060;	The value for variable "Presenting_Symptoms" for all samples is the same ("Vaginal bleeding").

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#10060;	Row 3: Fail
- "GSM46914	Alcohol_Consumption	No" is not found.

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

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
