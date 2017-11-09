<h1><center>testBranch</center></h1>
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

#### Results: **<font color="red">PASS</font>**
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

Executing parse.sh: 

&#10060;	parse.sh returned an error:
~~~bash
Traceback (most recent call last):
  File "parse.py", line 9, in <module>
    with open(expressionInfo, 'r')  as f1:
IOError: [Errno 2] No such file or directory: 'tmp/Expression'
gzip: metadata.tsv: No such file or directory
gzip: data.tsv: No such file or directory
~~~

