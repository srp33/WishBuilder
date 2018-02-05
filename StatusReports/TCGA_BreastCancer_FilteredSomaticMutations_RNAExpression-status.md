<h1><center>TCGA_BreastCancer_FilteredSomaticMutations_RNAExpression</center></h1>
<h2><center> Status: Complete </center></h2>
<center>Feb 05, 18. 11:02 MST</center>


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

&#9989;	test_metadata.tsv contains enough test cases (16; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	1/2-SBSRNA4	|	A1BG	|	A1BG-AS1	|	A1CF	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-3C-AAAU-01A-11R-A41B-07	|	5.54232446204596	|	12.9679516712473	|	3.14176915832577	|	0.00520202913308217	|
|	TCGA-3C-AALI-01A-11R-A41B-07	|	3.39482819338405	|	17.1577035101616	|	4.32682026222599	|	0.118286519300192	|
|	TCGA-3C-AALJ-01A-31R-A41B-07	|	2.50640106626595	|	31.6096061992498	|	2.866475585645	|	0.102975760042304	|
|	TCGA-3C-AALK-01A-11R-A41B-07	|	1.84821794433028	|	13.2984130137491	|	1.61465988642	|	0.02062411320675	|

**Columns: 23369 Rows: 944**

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
|	TCGA-3C-AAAU-01A-11R-A41B-07	|	form_completion_date	|	2014-1-13	|
|	TCGA-3C-AAAU-01A-11R-A41B-07	|	prospective_collection	|	NO	|
|	TCGA-3C-AAAU-01A-11R-A41B-07	|	retrospective_collection	|	YES	|
|	TCGA-3C-AAAU-01A-11R-A41B-07	|	gender	|	FEMALE	|

**Columns: 3 Rows: 118957**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "days_to_initial_pathologic_diagnosis" for all samples is the same ("0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "informed_consent_verified" for all samples is the same ("YES"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "tumor_tissue_site" for all samples is the same ("Breast"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "clinical_T" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "disease_code" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "project_code" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_er_positivity_define_method" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_pr_positivity_other_scale" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_pr_positivity_define_method" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_her2_positivity_other_scale" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_her2_positivity_method" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_her2_signal_number" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_cent_17_signal_number" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "her2_cent17_counted_cells_count" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_cent17_her2_other_scale" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "nte_her2_fish_define_method" for all samples is the same ("[Not Available]"). This variable has been removed from metadata.tsv.gz</p>

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

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
