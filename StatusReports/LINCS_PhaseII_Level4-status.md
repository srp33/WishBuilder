<h1><center>LINCS_PhaseII_Level4</center></h1>
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

&#10060;	Row 7 of "test_data.tsv" should contain exactly three columns.

&#9989;	test_data.tsv contains enough unique samples to test

&#10060;	"REP.A028_YAPC_24H_X1_B25:G09" does not have enough features to test (min: 2)

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (15; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	DDR1	|	PAX8	|	GUCA1A	|	EPHB3	|
|	---	|	---	|	---	|	---	|	---	|
|	REP.A001_A375_24H_X1_B22:A03	|	14.820400238	|	0.0	|	-1.33200001717	|	1.44690001011	|
|	REP.A001_A375_24H_X1_B22:A04	|	-0.519999980927	|	4.31339979172	|	-1.82099997997	|	-1.32109999657	|
|	REP.A001_A375_24H_X1_B22:A05	|	-1.03690004349	|	-1.12460005283	|	0.805400013924	|	-0.745700001717	|
|	REP.A001_A375_24H_X1_B22:A06	|	-0.300500005484	|	-0.467000007629	|	-0.443899989128	|	-0.776799976826	|

**Columns: 12329 Rows: 345977**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 7 of "test_data.tsv" does not contain 3 columns

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#10060;	Row: 7 - Sample "REP.A028_YAPC_24H_X1_B25:G09" is not found in data.tsv.gz

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	LJP005_A375_24H_X1_B19:A03	|	cell_id	|	A375	|
|	LJP005_A375_24H_X1_B19:A03	|	cell_type	|	cell line	|
|	LJP005_A375_24H_X1_B19:A03	|	base_cell_id	|	A375	|
|	LJP005_A375_24H_X1_B19:A03	|	sample_type	|	tumor	|

**Columns: 3 Rows: 7766814**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "pert_time_unit" for all samples is the same ("h"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

&#9989;	Row 13: Success

&#9989;	Row 14: Success

&#9989;	Row 15: Success

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
