<h1><center>GSE62944_Tumor_TPM</center></h1>
<h2><center> Status: In Progress </center></h2>


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

&#10060;	"TCGA-ZX-AA5X-01A-11R-A42T-07" does not have enough features to test (min: 2)

&#10060;	"TCGA-02-0047-01A-01R-1849-01" does not have enough features to test (min: 2)

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	SampleID	|	1/2-SBSRNA4	|	A1BG	|	A1BG-AS1	|	A1CF	|
|	---	|	---	|	---	|	---	|	---	|
|	TCGA-02-0047-01A-01R-1849-01	|	2.34180779897709	|	11.7173931223676	|	1.33274150888264	|	0.00783961263378836	|
|	TCGA-02-0055-01A-01R-1849-01	|	1.64575215578575	|	24.7763572132346	|	1.08603706301478	|	0.015495311808889	|
|	TCGA-02-2483-01A-01R-1849-01	|	2.43263380829254	|	20.2648719245462	|	1.09297209133143	|	0.00479039331850954	|
|	TCGA-02-2485-01A-01R-1849-01	|	2.04036406475485	|	5.1177123833555	|	0.707189363771972	|	0.00585469442145148	|

**Columns: 23369 Rows: 9265**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	First column of file must be titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	SampleID	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	TCGA-02-0047-01A-01R-1849-01	|	Cancer_Type	|	GBM	|
|	TCGA-02-0047-01A-01R-1849-01	|	form_completion_date	|	2008-12-16	|
|	TCGA-02-0047-01A-01R-1849-01	|	prospective_collection	|	[Not Available]	|
|	TCGA-02-0047-01A-01R-1849-01	|	retrospective_collection	|	[Not Available]	|

**Columns: 3 Rows: 645495**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	First column of file must be titled "Sample"

&#10060;	All values for variable "number_of_lymphnodes_positive_by_ihc" are the same("[Not Available]").

&#10060;	All values for variable "disease_code" are the same("[Not Available]").

&#10060;	All values for variable "nte_pr_positivity_define_method" are the same("[Not Available]").

&#10060;	All values for variable "her2_cent17_counted_cells_count" are the same("[Not Available]").

&#10060;	All values for variable "initial_pathologic_dx_days_to" are the same("0").

&#10060;	All values for variable "days_to_laboratory_procedure_tumor_marker_squamous_cell_carcinoma_antigen_result" are the same("[Not Available]").

&#10060;	All values for variable "extranodal_involvement" are the same("[Not Applicable]").

&#10060;	All values for variable "nte_her2_positivity_method" are the same("[Not Available]").

&#10060;	All values for variable "nte_pr_positivity_other_scale" are the same("[Not Available]").

&#10060;	All values for variable "nte_her2_signal_number" are the same("[Not Available]").

&#10060;	All values for variable "nte_er_positivity_define_method" are the same("[Not Available]").

&#10060;	All values for variable "history_chemical_exposure_other" are the same("[Not Available]").

&#10060;	All values for variable "informed_consent_verified" are the same("YES").

&#10060;	All values for variable "scca_tumor_marker" are the same("[Not Available]").

&#10060;	All values for variable "project_code" are the same("[Not Available]").

&#10060;	All values for variable "eml4_alk_translocation_variant" are the same("[Not Available]").

&#10060;	All values for variable "nte_cent_17_signal_number" are the same("[Not Available]").

&#10060;	All values for variable "diff_count_not_present_reason" are the same("[Not Available]").

&#10060;	All values for variable "nte_her2_fish_define_method" are the same("[Not Available]").

&#10060;	All values for variable "pathologic_M" are the same("[Not Applicable]").

&#10060;	All values for variable "nte_her2_positivity_other_scale" are the same("[Not Available]").

&#10060;	All values for variable "history_immunosuppresive_dx_other" are the same("[Not Available]").

&#10060;	All values for variable "nte_cent17_her2_other_scale" are the same("[Not Available]").

&#10060;	All values for variable "ajcc_clinical_tumor_stage" are the same("[Not Applicable]").

&#10060;	All values for variable "cells_used_for_analysis_source" are the same("Bone marrow aspirate").

&#10060;	All values for variable "pcr_primer_pairs_other" are the same("[Not Applicable]").

&#10060;	All values for variable "cause_of_death_other" are the same("[Not Available]").

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#10060;	Row 3: Fail
- "TCGA-A5-A0VQ-01A-11R-A104-07	form_completion_date	TCGA-A5-A0VQ" is not found.

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

&#10060;	Comma(s) exist in metadata.tsv.gz

&#9989;	No Commas in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
