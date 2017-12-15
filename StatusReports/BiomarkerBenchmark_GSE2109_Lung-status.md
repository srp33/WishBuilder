<h1><center>BiomarkerBenchmark_GSE2109_Lung</center></h1>
<h2><center> Status: Complete </center></h2>


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

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM38100	|	1.40368261764706	|	-0.25811851375	|	2.23105485222222	|	0.4314917628125	|
|	GSM38103	|	1.92959003882353	|	0.02999554625	|	1.84192114111111	|	0.8087353546875	|
|	GSM38104	|	1.85159212117647	|	-0.2049791175	|	2.02616687	|	0.3431711746875	|
|	GSM46824	|	1.90478119705882	|	-0.2592340275	|	2.22703217444444	|	0.7706966209375	|

**Columns: 20025 Rows: 104**

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
|	GSM38100	|	Alcohol_Consumption	|	Yes	|
|	GSM38100	|	Days_from_Patient_Diagnosis_to_Excision	|	24	|
|	GSM38100	|	Ethnic_Background	|	Caucasian	|
|	GSM38100	|	Family_History_of_Cancer	|	Yes	|

**Columns: 3 Rows: 1921**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Ethnic_Background" for all samples is the same ("Caucasian"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Pathological_Stage_During_or_Following_Multimodality_Therapy" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Primary_Site" for all samples is the same ("Lung"). This variable has been removed from metadata.tsv.gz</p>

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
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
