<h1><center>LINCS_PhaseII_Level3</center></h1>

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

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (15; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	DDR1	|	PAX8	|	GUCA1A	|	EPHB3	|
|	---	|	---	|	---	|	---	|	---	|
|	LJP005_A375_24H_X1_B19:A03	|	6.54829978943	|	4.46420001984	|	4.82719993591	|	5.97429990768	|
|	LPROT001_A375_6H_X1_B20:B03	|	5.33190011978	|	5.86509990692	|	6.20599985123	|	8.62740039825	|
|	LPROT001_A375_6H_X1_B20:B05	|	5.85659980774	|	6.10020017624	|	5.93030023575	|	9.55449962616	|
|	LPROT002_A375_6H_X1_B22:B03	|	6.82100009918	|	3.99130010605	|	4.17999982834	|	6.34259986877	|

**Columns: 12329 Rows: 345632**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 10 of "test_data.tsv" does not contain 3 columns

#### Results: **<font color="red">FAIL</font>**
---&#10060;	Row 11 of "test_data.tsv" does not contain 3 columns

#### Results: **<font color="red">FAIL</font>**
---&#10060;	Row 12 of "test_data.tsv" does not contain 3 columns

#### Results: **<font color="red">FAIL</font>**
---&#9989;	Row: 3 - Success

&#9989;	Row: 4 - Success

&#9989;	Row: 5 - Success

&#9989;	Row: 6 - Success

&#9989;	Row: 1 - Success

&#9989;	Row: 2 - Success

&#9989;	Row: 7 - Success

&#9989;	Row: 8 - Success

&#9989;	Row: 9 - Success

&#10060;	Row: 9 - Sample "3" is not found in data.tsv.gz

&#10060;	Row: 9 - Sample "_" is not found in data.tsv.gz

&#10060;	Row: 9 - Sample "2" is not found in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	LJP005_A375_24H_X1_B19:A03	|	cell_id	|	A375	|
|	LJP005_A375_24H_X1_B19:A03	|	cell_type	|	cell line	|
|	LJP005_A375_24H_X1_B19:A03	|	base_cell_id	|	A375	|
|	LJP005_A375_24H_X1_B19:A03	|	sample_type	|	tumor	|

**Columns: 3 Rows: 7778851**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	All values for variable "pert_time_unit" are the same("h").

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#10060;	Row 9: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	cell_id	YAPC" is not found.

&#10060;	Row 10: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	cell_type	cell line" is not found.

&#10060;	Row 11: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	donor_sex	M" is not found.

&#10060;	Row 12: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	det_plate	REP.A028_YAPC_24H_X3_B25" is not found.

&#10060;	Row 13: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	pert_id	BRD-A97502381" is not found.

&#10060;	Row 14: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	inchi_key	FMCRMSOQAVOHRD-SBGISONWSA-M" is not found.

&#10060;	Row 15: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	pert_iname	cyanocobalamin" is not found.

#### Results: **<font color="red">FAIL</font>**
---
