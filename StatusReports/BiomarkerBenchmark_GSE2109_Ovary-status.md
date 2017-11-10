<h1><center>BiomarkerBenchmark_GSE2109_Ovary</center></h1>
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
|	GSM38071	|	2.68516924882353	|	-0.24817909	|	2.63589104777778	|	0.3856919240625	|
|	GSM38088	|	2.03102289647059	|	-0.1970764175	|	2.74216320444444	|	0.4001315015625	|
|	GSM46815	|	1.70166555235294	|	-0.1766490275	|	2.81732544111111	|	0.691595185	|
|	GSM46830	|	1.99339338882353	|	-0.14836305	|	2.24644423	|	0.317661369375	|

**Columns: 20025 Rows: 154**

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
|	GSM38071	|	Alcohol_Consumption	|	Yes	|
|	GSM38071	|	Days_from_Patient_Diagnosis_to_Excision	|	11	|
|	GSM38071	|	Ethnic_Background	|	Caucasian	|
|	GSM38071	|	Family_History_of_Cancer	|	Yes	|

**Columns: 3 Rows: 2317**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	All values for variable "Primary_Site" are the same("Ovary").

&#10060;	All values for variable "Grade" are the same("1").

&#10060;	All values for variable "Clinical_Stage_During_or_Following_Multimodality_Therapy" are the same("No").

&#10060;	All values for variable "Type_of_Tobacco_Use" are the same("Cigarettes").

&#10060;	All values for variable "Clinical_M" are the same("0").

&#10060;	All values for variable "Ethnic_Background" are the same("Caucasian").

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

&#10060;	Comma(s) exist in metadata.tsv.gz

&#9989;	No Commas in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
