<h1><center>BiomarkerBenchmark_GSE63885</center></h1>
<h2><center> Status: Complete </center></h2>
<center>Mar 05, 18. 15:03 MST</center>


### Testing Directory . . .

#### Results: PASS
---
### Testing Configuration File . . .

&#9989;	config.yaml contains all necessary configurations.

&#9989;	Title is less than 300 characters

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

&#9989;	test_metadata.tsv contains enough test cases (10; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM1559299	|	1.58190624764706	|	-0.15402261125	|	2.48422321444444	|	0.4192952234375	|
|	GSM1559300	|	2.13530725882353	|	-0.04666310125	|	3.01121228	|	0.2587855653125	|
|	GSM1559301	|	2.08582202823529	|	-0.21383749125	|	2.52594365	|	0.459416181875	|
|	GSM1559302	|	2.26551759352941	|	-0.08622420625	|	2.42361450666667	|	0.4584177853125	|

**Columns: 20025 Rows: 93**

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
|	GSM1559299	|	adjuwant_chemotherapy	|	platinum/cyclophosphamide	|
|	GSM1559299	|	brca1_mutation	|	no mutation	|
|	GSM1559299	|	clinical_status_at_last_follow-up_awd_-_alive_with_disease;_dod_-_dead_from_disease;_ned_-_no_evidence_of_disease	|	DOD	|
|	GSM1559299	|	clinical_status_post_1st_line_chemotherapy_cr_-_complete_response;_pr_-_partial_response;_sd_-_stable_disease;_p_-_progression	|	P	|

**Columns: 3 Rows: 931**

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

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
