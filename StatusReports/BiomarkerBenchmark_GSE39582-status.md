<h1><center>BiomarkerBenchmark_GSE39582</center></h1>
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
|	GSM971957	|	2.11019764117647	|	0.29710354625	|	2.54086968444444	|	0.8408434203125	|
|	GSM971958	|	2.69180617705882	|	0.03353052625	|	2.76094172666667	|	0.444017269375	|
|	GSM971959	|	2.30993825352941	|	-0.148700045	|	2.49540275111111	|	0.3675600628125	|
|	GSM971960	|	3.40408548235294	|	0.2708252125	|	2.63223672333333	|	0.6184695296875	|

**Columns: 20025 Rows: 557**

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
|	GSM971957	|	age.at.diagnosis_year	|	34.5	|
|	GSM971957	|	braf.mutation	|	WT	|
|	GSM971957	|	chemotherapy.adjuvant	|	N	|
|	GSM971957	|	cimp.status	|	-	|

**Columns: 3 Rows: 12047**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "braf.mutation.exon.number" for all samples is the same ("c.1799T>A"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "braf.mutation.protein" for all samples is the same ("p.V600E"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "braf.mutation.dna" for all samples is the same ("c.1799T>A"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#10060;	Row 5: Fail
- "GSM972123	age.at.diagnosis_year	77" is not found.

&#9989;	Row 6: Success

&#10060;	Row 7: Fail
- "GSM972126	age.at.diagnosis_year	69" is not found.

&#10060;	Row 8: Fail
- "GSM972126	tumor.location	proximal" is not found.

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
