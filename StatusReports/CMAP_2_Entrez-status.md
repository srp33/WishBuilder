<h1><center>CMAP_2_Entrez</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Jan 31, 18 17:01PM MST</center>


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

|	Sample	|	AKT3	|	MED6	|	NR2E3	|	NAALAD2	|
|	---	|	---	|	---	|	---	|	---	|
|	5202764005791175120104.E08	|	-0.07604248	|	1.0043152	|	-0.06929116	|	-0.19717948	|
|	5202764005791175120104.E10	|	-0.11460035	|	1.28248579	|	-0.03530519	|	-0.1545126	|
|	5202764005791175120104.E11	|	-0.09928488	|	1.29957722	|	-0.0648402	|	-0.11181129	|
|	5202764005791175120104.E12	|	-0.10193789	|	1.23273062	|	-0.05491299	|	-0.10846203	|

**Columns: 0 Rows: 1**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	NA is in data.tsv.gz column headers more than once

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	5202764005791175120104.E08	|	Perturbagen	|	vorinostat	|
|	5202764005791175120104.E08	|	Concentration	|	0.00001	|
|	5202764005791175120104.E08	|	Cell Line Name	|	MCF7	|
|	5202764005791175120104.E08	|	Batch	|	506	|

**Columns: 3 Rows: 34325**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

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

&#9989;	Row 16: Success

&#9989;	Row 17: Success

&#9989;	Row 18: Success

#### Results: PASS
---
### Comparing samples in both files . . .

&#10060;	 Sample "5500024034290101707050.F06" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "5500024037498121108437.D09" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "5500024031723100807769.F11" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "614615111406.G02" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "5500024031723100807773.B05" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "5500024024213121906563.E09" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "5500024024213121906560.E05" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "5500024031723100807773.A01" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "5500024031723100807776.H04" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 7056</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
