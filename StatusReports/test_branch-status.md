<h1><center>test_branch</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Feb 26, 18 11:02AM MST</center>


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

&#10060;	test_data.tsv does not contain enough unique samples to test (min: 2)

&#10060;	test_data.tsv does not contain enough test cases. (6; min: 8)

&#10060;	Row 1 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	Row 2 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	Row 3 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	Row 4 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	Row 5 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	Row 6 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	test_metadata.tsv does not contain enough unique samples to test (min: 2)

&#10060;	test_metadata.tsv does not contain enough test cases. (6; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	gene1	|	gene2	|	gene3	|	gene4	|
|	---	|	---	|	---	|	---	|	---	|
|	1	|	1	|	2	|	3	|	4	|
|	2	|	11	|	22	|	33	|	44	|
|	3	|	111	|	222	|	333	|	444	|
|	4	|	1111	|	2222	|	3333	|	4444	|

**Columns: 6 Rows: 6**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 1 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 2 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 3 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 4 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 5 of "test_data.tsv" does not contain 3 columns

&#10060;	Row 6 of "test_data.tsv" does not contain 3 columns

&#10060;	Row: 1 - Sample "1       age     10" is not found in data.tsv.gz

&#10060;	Row: 2 - Sample "1       color   blue" is not found in data.tsv.gz

&#10060;	Row: 3 - Sample "2       age     20" is not found in data.tsv.gz

&#10060;	Row: 4 - Sample "2       color   green" is not found in data.tsv.gz

&#10060;	Row: 5 - Sample "3       age     30" is not found in data.tsv.gz

&#10060;	Row: 6 - Sample "3       color   red" is not found in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	1	|	age	|	10	|
|	1	|	color	|	blue	|
|	2	|	age	|	20	|
|	2	|	color	|	green	|

**Columns: 3 Rows: 11**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 1: Fail
- "1       gne1   1" is not found.

&#10060;	Row 2: Fail
- "1       gene2   11" is not found.

&#10060;	Row 3: Fail
- "2       gene1   2" is not found.

&#10060;	Row 4: Fail
- "2       gene2   22" is not found.

&#10060;	Row 5: Fail
- "5       gene5   55555" is not found.

&#10060;	Row 6: Fail
- "5       gene3   555" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
