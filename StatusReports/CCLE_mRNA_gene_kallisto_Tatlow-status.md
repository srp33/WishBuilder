<h1><center>CCLE_mRNA_gene_kallisto_Tatlow</center></h1>
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

|	Sample	|	ARF5	|	M6PR	|	ESRRA	|	FKBP4	|
|	---	|	---	|	---	|	---	|	---	|
|	COR-L24	|	185.743215	|	102.686215319	|	18.638011	|	114.562929	|
|	HSC-3	|	111.760973	|	137.565799	|	33.803128	|	90.439629	|
|	KMS-11	|	137.16564	|	120.717231	|	23.442103	|	168.42325	|
|	C2BBe1	|	230.498743	|	211.752821304	|	35.423889	|	142.868279	|

**Columns: 58685 Rows: 935**

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

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	COR-L24	|	Gender	|	M	|
|	COR-L24	|	Site Primary	|	lung	|
|	COR-L24	|	Histology	|	carcinoma	|
|	COR-L24	|	Hist Subtype1	|	small_cell_carcinoma	|

**Columns: 3 Rows: 8321**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Hybrid Capture Sequencing" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Oncomap" for all samples is the same ("yes"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#10060;	Row 7: Fail
- "COLO-680N	Gender	F" is not found.

&#10060;	Row 8: Fail
- "COLO-680N	Hybrid Capture Sequencing	yes" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "UO-31" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "SF268" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "EKVX" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "COLO-680N" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "MOLT-3" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "SF539" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "HOP-92" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "HOP-62" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 Sample "RS4_11" is in "data.tsv.gz" but not in "metadata.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 11</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
