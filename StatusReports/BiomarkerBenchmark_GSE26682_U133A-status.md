<h1><center>BiomarkerBenchmark_GSE26682_U133A</center></h1>
<h2><center> Status: Complete </center></h2>


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
|	GSM656544	|	1.80085877176471	|	-0.2336191225	|	2.54590516888889	|	0.305379200434783	|
|	GSM656547	|	1.91316862058824	|	-0.238365205	|	2.51419520777778	|	0.196926308695652	|
|	GSM656562	|	1.26774902647059	|	-0.044878185	|	1.75252909222222	|	0.152728137826087	|
|	GSM656563	|	1.82024041294118	|	-0.2497113225	|	2.16285579333333	|	0.141793532173913	|

**Columns: 11833 Rows: 141**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row: 1 - Success

&#9989;	Row: 2 - Success

&#9989;	Row: 3 - Success

&#9989;	Row: 4 - Success

&#9989;	Row: 5 - Success

&#9989;	Row: 6 - Success

&#9989;	Row: 7 - Success

&#9989;	Row: 8 - Success

#### Results: PASS
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	GSM656544	|	age	|	76	|
|	GSM656544	|	gender	|	Female	|
|	GSM656544	|	microsatellite_instability_msi_status	|	Stable [MSS]	|
|	GSM656547	|	age	|	68	|

**Columns: 3 Rows: 421**

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

#### Results: PASS
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
