<h1><center>BiomarkerBenchmark_GSE46691</center></h1>
## Status: Complete
### Testing Directory . . .

#### Results: PASS
---
### Testing file paths:

&#9989;	test_data.tsv exists.

&#9989;	test_metadata.tsv exists.

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

*Running user code . . .*

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
|	GSM1134064	|	0.417440489230769	|	0.0106500273333333	|	0.684045122285714	|	0.292820167818182	|
|	GSM1134065	|	0.348597424871795	|	-0.136350598	|	0.33116253	|	0.243901822	|
|	GSM1134066	|	0.408818731538462	|	-0.00549893233333333	|	0.480663864285714	|	0.338286896727273	|
|	GSM1134067	|	0.155328175897436	|	0.0146407966666667	|	0.282751727714286	|	0.268711702545455	|

**Columns: 16633 Rows: 546**

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
|	GSM1134064	|	gleason_score	|	7	|
|	GSM1134064	|	metastatic_event	|	1	|
|	GSM1134065	|	gleason_score	|	6	|
|	GSM1134065	|	metastatic_event	|	0	|

**Columns: 3 Rows: 1091**

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
### Comparing samples in both files . . .

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
