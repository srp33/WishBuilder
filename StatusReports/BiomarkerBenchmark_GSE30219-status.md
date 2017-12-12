<h1><center>BiomarkerBenchmark_GSE30219</center></h1>
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

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM1465989	|	2.05427252941176	|	-0.18814726625	|	2.13505803444444	|	0.523828755	|
|	GSM1465990	|	2.38591473470588	|	-0.22116824125	|	2.78432002888889	|	0.4807718146875	|
|	GSM1465991	|	2.50706494588235	|	-0.25247381375	|	2.61063488111111	|	0.78544667375	|
|	GSM1465992	|	1.36965303529412	|	-0.171055715	|	2.44443693666667	|	1.0092989790625	|

**Columns: 20025 Rows: 286**

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
|	GSM748053	|	age_at_surgery	|	62	|
|	GSM748053	|	disease_free_survival_in_months	|	121	|
|	GSM748053	|	follow-up_time_months	|	121	|
|	GSM748053	|	gender	|	F	|

**Columns: 3 Rows: 2825**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#10060;	Row 2: Fail
- "GSM1465989	tissue	lung tumour" is not found.

&#9989;	Row 3: Success

&#10060;	Row 4: Fail
- "GSM1465990	tissue	lung tumour" is not found.

&#9989;	Row 5: Success

&#10060;	Row 6: Fail
- "GSM748160	tissue	lung tumour" is not found.

&#9989;	Row 7: Success

&#10060;	Row 8: Fail
- "GSM748174	tissue	lung tumour" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
