<h1><center>BiomarkerBenchmark_GSE2109_Endometrium</center></h1>
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

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#10060;	"GSM152660       Tobacco_Use" does not have enough features to test (min: 2)

&#10060;	"GSM38067        Alcohol_Consumption" does not have enough features to test (min: 2)

&#10060;	"GSM76649        Tobacco_Use" does not have enough features to test (min: 2)

&#10060;	"GSM152660       Alcohol_Consumption" does not have enough features to test (min: 2)

&#10060;	"GSM38084        Alcohol_Consumption" does not have enough features to test (min: 2)

&#10060;	"GSM76649        Alcohol_Consumption" does not have enough features to test (min: 2)

&#10060;	"GSM38084        Tobacco_Use" does not have enough features to test (min: 2)

&#10060;	"GSM38067        Tobacco_Use" does not have enough features to test (min: 2)

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM38067	|	2.51174563411765	|	-0.06398938	|	2.41418058111111	|	0.532588206875	|
|	GSM38084	|	2.04430493	|	-0.17738299125	|	2.25459530444444	|	0.2675048278125	|
|	GSM46867	|	2.35919298411765	|	-0.10473930125	|	2.42252435777778	|	0.5238796334375	|
|	GSM46912	|	2.55878040764706	|	-0.2314555575	|	2.05281890111111	|	0.48969787375	|

**Columns: 20025 Rows: 52**

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
|	GSM38067	|	Alcohol_Consumption	|	Yes	|
|	GSM38067	|	Days_from_Patient_Diagnosis_to_Excision	|	42	|
|	GSM38067	|	Ethnic_Background	|	Caucasian	|
|	GSM38067	|	Family_History_of_Cancer	|	No	|

**Columns: 3 Rows: 719**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Histology" for all samples is the same ("Endometrioid carcinoma"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Clinical_Multiple_Tumors" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Clinical_Stage_During_or_Following_Multimodality_Therapy" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Type_of_Tobacco_Use" for all samples is the same ("Cigarettes"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Pathological_Multiple_Tumors" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Primary_Site" for all samples is the same ("Endometrium"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Clinical_N" for all samples is the same ("0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Pathological_Stage_During_or_Following_Multimodality_Therapy" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Ethnic_Background" for all samples is the same ("Caucasian"). This variable has been removed from metadata.tsv.gz</p>

&#10060;	Row 1: Fail
- "GSM38067        Alcohol_Consumption	Yes" is not found.

&#10060;	Row 2: Fail
- "GSM38067        Tobacco_Use	No" is not found.

&#10060;	Row 3: Fail
- "GSM38084        Alcohol_Consumption	No" is not found.

&#10060;	Row 4: Fail
- "GSM38084        Tobacco_Use	No" is not found.

&#10060;	Row 5: Fail
- "GSM152660       Alcohol_Consumption	Yes" is not found.

&#10060;	Row 6: Fail
- "GSM152660       Tobacco_Use	No" is not found.

&#10060;	Row 7: Fail
- "GSM76649        Alcohol_Consumption	No" is not found.

&#10060;	Row 8: Fail
- "GSM76649        Tobacco_Use	No" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
