<h1><center>CMAP_2_Entrez</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Jan 30, 18 17:01PM MST</center>


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

&#9989;	test_metadata.tsv contains enough test cases (18; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	5202764005791175120104.E08	|	-0.07604248	|	1.0043152	|	-0.06929116	|	-0.19717948	|
|	---	|	---	|	---	|	---	|	---	|
|	5202764005791175120104.E10	|	-0.11460035	|	1.28248579	|	-0.03530519	|	-0.1545126	|
|	5202764005791175120104.E11	|	-0.09928488	|	1.29957722	|	-0.0648402	|	-0.11181129	|
|	5202764005791175120104.E12	|	-0.10193789	|	1.23273062	|	-0.05491299	|	-0.10846203	|
|	5202764005791175120104.D07	|	-0.12884382	|	0.96603081	|	-0.11027136	|	-0.0751726	|

**Columns: 12081 Rows: 7056**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	First column of file must be titled "Sample"

&#10060;	Row: 1 - Sample "5202764005791175120104.E08" is not found in data.tsv.gz

&#10060;	Row: 2 - Sample "5202764005791175120104.E08" is not found in data.tsv.gz

&#10060;	Row: 3 - AKT3 is not found in "data.tsv.gz" column headers

&#10060;	Row: 4 - NAT1 is not found in "data.tsv.gz" column headers

&#10060;	Row: 5 - AKT3 is not found in "data.tsv.gz" column headers

&#10060;	Row: 6 - NAT1 is not found in "data.tsv.gz" column headers

&#10060;	Row: 7 - AKT3 is not found in "data.tsv.gz" column headers

&#10060;	Row: 8 - NAT1 is not found in "data.tsv.gz" column headers

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	5202764005791175120104.E08	|	Perturbagen	|	vorinostat	|
|	---	|	---	|	---	|
|	5202764005791175120104.E08	|	Concentration	|	0.00001	|
|	5202764005791175120104.E08	|	Cell Line Name	|	MCF7	|
|	5202764005791175120104.E08	|	Batch	|	506	|
|	5202764005791175120104.E08	|	Array	|	HT_HG-U133A_EA	|

**Columns: 3 Rows: 34324**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	First column of file must be titled "Sample"

&#10060;	Row 1: Fail
- "5202764005791175120104.E08	Perturbagen	vorinostat" is not found.

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

&#9989;	Row 16: Success

&#9989;	Row 17: Success

&#9989;	Row 18: Success

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#10060;	 Sample "5202764005791175120104.E08" is in "metadata.tsv.gz" but not in "data.tsv.gz"

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
