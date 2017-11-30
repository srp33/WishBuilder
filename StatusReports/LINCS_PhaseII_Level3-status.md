<h1><center>LINCS_PhaseII_Level3</center></h1>
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

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (15; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|		|	DDR1	|	PAX8	|	GUCA1A	|	EPHB3	|
|	---	|	---	|	---	|	---	|	---	|
|	REP.A001_A375_24H_X1_B22:A03	|	9.36979961395	|	4.41800022125	|	4.15040016174	|	6.43020009995	|
|	REP.A001_A375_24H_X1_B22:A04	|	6.86800003052	|	5.36189985275	|	4.00960016251	|	5.30740022659	|
|	REP.A001_A375_24H_X1_B22:A05	|	6.78369998932	|	4.17189979553	|	4.76579999924	|	5.5408000946	|
|	REP.A001_A375_24H_X1_B22:A06	|	6.90380001068	|	4.31580018997	|	4.4060997963	|	5.52820014954	|

**Columns: 12329 Rows: 7**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	First column of file must be titled "Sample"

&#10060;	Row: 1 - Sample "LJP009_PC3_24H_X2_B20:O08" is not found in data.tsv.gz

&#10060;	Row: 2 - Sample "LJP009_PC3_24H_X2_B20:O08" is not found in data.tsv.gz

&#10060;	Row: 3 - Sample "LJP005_A375_24H_X1_B19:A03" is not found in data.tsv.gz

&#10060;	Row: 4 - Sample "LJP005_A375_24H_X1_B19:A03" is not found in data.tsv.gz

&#10060;	Row: 5 - Sample "LJP006_A375_24H_X1_B19:L06" is not found in data.tsv.gz

&#10060;	Row: 6 - Sample "LJP006_A375_24H_X1_B19:L06" is not found in data.tsv.gz

&#10060;	Row: 7 - Sample "REP.A028_YAPC_24H_X1_B25:G09" is not found in data.tsv.gz

&#10060;	Row: 8 - Sample "REP.A028_YAPC_24H_X1_B25:G09" is not found in data.tsv.gz

&#10060;	Row: 9 - Sample "REP.A028_YAPC_24H_X3_B25:B12" is not found in data.tsv.gz

&#10060;	Row: 10 - Sample "REP.A028_YAPC_24H_X3_B25:B12" is not found in data.tsv.gz

&#10060;	Row: 11 - Sample "LJP006_A549_24H_X2_B19:J22" is not found in data.tsv.gz

&#10060;	Row: 12 - Sample "LJP006_A549_24H_X2_B19:J22" is not found in data.tsv.gz

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
### Checking Files for commas . . .

<p><font color="orange" size="+2">&#9888;	</font>Comma(s) exist in "metadata.tsv.gz". This may create an issue if exported in .csv format.</p>

#### Results: **<font color="orange">WARNED</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "REP.A017_MCF7_24H_X1_B23:L04" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "REP.A026_A375_24H_X1_B25:C18" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "LJP005_SKBR3_3H_X3_B17:O17" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "REP.A027_MCF7_24H_X1_B25:N03" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "REP.A016_HELA_24H_X3_B23:L14" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "LJP006_SKBR3_3H_X1_B17:A24" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "REP.A006_PC3_24H_X2_B22:C02" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "LJP006_BT20_3H_X2_B17:K08" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "REP.A028_PC3_24H_X1_B25:O21" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 345970</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
