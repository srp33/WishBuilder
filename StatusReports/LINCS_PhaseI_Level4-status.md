<h1><center>LINCS_PhaseI_Level4</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Feb 28, 18 11:02AM MST</center>


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

Executing parse.sh: 

&#10060;	parse.sh returned an error:
~~~bash
Could not find conda environment: lincs_env
You can list all discoverable environments with `conda info --envs`.

Traceback (most recent call last):
  File "parse.py", line 1, in <module>
    import h5py
ImportError: No module named h5py
~~~

