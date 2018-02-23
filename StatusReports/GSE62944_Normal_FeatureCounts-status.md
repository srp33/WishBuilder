<h1><center>GSE62944_Normal_FeatureCounts</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Feb 23, 18 16:02PM MST</center>


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
Error in contrib.url(repos, type) : 
  trying to use CRAN without setting a mirror
Calls: install.packages -> grep -> contrib.url
Execution halted
Traceback (most recent call last):
  File "parse.py", line 12, in <module>
    with open(namesToAbbreviations, 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'tmp/nameToAbbreviation.txt'
~~~

