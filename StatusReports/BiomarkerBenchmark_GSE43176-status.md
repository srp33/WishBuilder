<h1><center>BiomarkerBenchmark_GSE43176</center></h1>
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
|	GSM1057836	|	-0.04165015	|	-0.11731505125	|	0.74634068	|	-0.10284184173913	|
|	GSM1057837	|	-0.102259795882353	|	-0.2626097925	|	1.11522876333333	|	-0.0383493347826087	|
|	GSM1057838	|	-0.222879033529412	|	-0.3286507475	|	1.06145151111111	|	-0.0790448365217391	|
|	GSM1057839	|	-0.0998797111764706	|	-0.22587852	|	1.21281470444444	|	0.06549571	|

**Columns: 11833 Rows: 104**

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
|	GSM1057836	|	cytogenetics	|	45,X,-Y,t(8;21)(q22;q22),del(10)(p14)	|
|	GSM1057836	|	disease_state	|	AML	|
|	GSM1057836	|	fab	|	M4E	|
|	GSM1057836	|	kras_status	|	KRAS wild type	|

**Columns: 3 Rows: 614**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	All values for variable "kras_status" are the same("KRAS wild type").

&#10060;	All values for variable "disease_state" are the same("AML").

&#10060;	Row 1: Fail
- "GSM1057836	cytogenetic	45,X,-Y,t(8;21)(q22;q22),del(10)(p14)" is not found.

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
