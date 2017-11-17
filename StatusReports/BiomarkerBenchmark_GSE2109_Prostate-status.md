<h1><center>BiomarkerBenchmark_GSE2109_Prostate</center></h1>
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
|	GSM38079	|	1.88023305705882	|	-0.27722608	|	1.88733032333333	|	0.3769980525	|
|	GSM46837	|	1.49190971470588	|	-0.2337158125	|	2.36947264444444	|	1.4301921496875	|
|	GSM46866	|	2.06201953529412	|	-0.19376123625	|	2.22562798	|	0.5496713615625	|
|	GSM53061	|	1.46081964764706	|	-0.1735639225	|	1.92268529666667	|	0.2441607125	|

**Columns: 20025 Rows: 77**

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
|	GSM38079	|	Number_of_years_PSA_Tested	|	11-15	|
|	GSM38079	|	Alcohol_Consumption	|	Yes	|
|	GSM38079	|	Cancer_discovered_by_digital_exam	|	Yes	|
|	GSM38079	|	Days_from_Patient_Diagnosis_to_Excision	|	21	|

**Columns: 3 Rows: 1426**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888; </font>The value for variable "Clinical_Stage_During_or_Following_Multimodality_Therapy" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz</p>

<font color="orange">&#9888;	</font>The value for variable "Current_status_of_disease" for all samples is the same ("Under Therapy"). This variable has been removed from metadata.tsv.gz

<font color="orange">&#9888;	</font>The value for variable "Pathological_Stage_During_or_Following_Multimodality_Therapy" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz

<font color="orange">&#9888;	</font>The value for variable "Clinical_Multiple_Tumors" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz

<font color="orange">&#9888;	</font>The value for variable "Pathological_Multiple_Tumors" for all samples is the same ("No"). This variable has been removed from metadata.tsv.gz

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
### Making sure no commas exist in either file . . .

<font color="orange">&#9888;</font>	Comma(s) exist in "metadata.tsv.gz". This may create an issue if exported in .csv format.

#### Results: **<font color="orange">WARNED</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
