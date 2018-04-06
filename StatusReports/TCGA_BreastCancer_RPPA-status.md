<h1><center>TCGA_BreastCancer_RPPA</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Apr 06, 18 16:04PM MST</center>


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

Executing parse.sh: 

&#10060;	parse.sh returned an error:
~~~bash
python3: can't open file 'keep_common_samples.py': [Errno 2] No such file or directory
~~~

