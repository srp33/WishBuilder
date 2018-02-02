<h1><center>METABRIC_cBio</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Feb 02, 18 13:02PM MST</center>


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

&#10060;	Row 1 of "test_data.tsv" should contain exactly three columns.

&#10060;	Row 2 of "test_data.tsv" should contain exactly three columns.

&#10060;	Row 3 of "test_data.tsv" should contain exactly three columns.

&#10060;	Row 4 of "test_data.tsv" should contain exactly three columns.

&#10060;	Row 5 of "test_data.tsv" should contain exactly three columns.

&#10060;	Row 6 of "test_data.tsv" should contain exactly three columns.

&#10060;	Row 7 of "test_data.tsv" should contain exactly three columns.

&#10060;	Row 8 of "test_data.tsv" should contain exactly three columns.

&#10060;	test_data.tsv does not contain enough unique samples to test (min: 2)

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#10060;	Row 9 of "test_metadata.tsv" should contain exactly three columns.

&#9989;	test_metadata.tsv contains enough unique samples to test

&#10060;	"MB-6020" does not have enough features to test (min: 2)

&#10060;	"MB-0906" does not have enough features to test (min: 2)

&#10060;	"MB-0045" does not have enough features to test (min: 2)

&#9989;	test_metadata.tsv contains enough test cases (10; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	1-Mar	|	1-Sep	|	10-Mar	|	10-Sep	|
|	---	|	---	|	---	|	---	|	---	|
|	MB-0000	|	5.637055414	|	5.5122099	|	5.235735917	|	7.180623224	|
|	MB-0002	|	5.52651759	|	5.483681622	|	5.168002061	|	7.178667891	|
|	MB-0005	|	6.332868835	|	5.150019856	|	5.175685045	|	7.089595223	|
|	MB-0006	|	6.048051079	|	5.637538225	|	5.215697492	|	6.621642185	|

**Columns: 24368 Rows: 1905**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 1 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 2 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 3 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 4 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 5 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 6 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 7 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 8 of "test_data.tsv" does not contain 3 columns

&#10060;	Row: 1 - Sample "MB-0362" is not found in data.tsv.gz

&#10060;	Row: 2 - Sample "MB-0346" is not found in data.tsv.gz

&#10060;	Row: 3 - Sample "MB-0386" is not found in data.tsv.gz

&#10060;	Row: 4 - Sample "MB-0574" is not found in data.tsv.gz

&#10060;	Row: 5 - Sample "MB-5453" is not found in data.tsv.gz

&#10060;	Row: 6 - Sample "MB-5471" is not found in data.tsv.gz

&#10060;	Row: 7 - Sample "MB-5127" is not found in data.tsv.gz

&#10060;	Row: 8 - Sample "MB-4313" is not found in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	MB-0000	|	INTCLUST	|	4ER+	|
|	MB-0000	|	GRADE	|	3	|
|	MB-0000	|	LATERALITY	|	r	|
|	MB-0000	|	CHEMOTHERAPY	|	NO	|

**Columns: 3 Rows: 11984852**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "SomaticMutation__NRAS__Variant_Classification" for all samples is the same ("Missense_Mutation"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "SomaticMutation__AGTR2__Variant_Classification" for all samples is the same ("Missense_Mutation"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "SomaticMutation__KRAS__Variant_Classification" for all samples is the same ("Missense_Mutation"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "SAMPLE_TYPE" for all samples is the same ("Primary"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#10060;	Row 7: Fail
- "MB-6020	CNA__ZZZ3	High-level amplification" is not found.

&#9989;	Row 8: Success

&#10060;	Row 9: Fail
- "MB-7299 HISTOLOGICAL_SUBTYPE	IDC" is not found.

&#9989;	Row 10: Success

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

&#10060;	"brca_metabric" should have been deleted during cleanup.

#### Results: **<font color="red">FAIL</font>**
---
