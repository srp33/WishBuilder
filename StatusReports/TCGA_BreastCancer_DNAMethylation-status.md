<h1><center>TCGA_BreastCancer_DNAMethylation</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Apr 25, 18 14:04PM MST</center>


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

Attaching package: ‘dplyr’

The following objects are masked from ‘package:stats’:

    filter, lag

The following objects are masked from ‘package:base’:

    intersect, setdiff, setequal, union


Attaching package: ‘tidyselect’

The following objects are masked from ‘package:dplyr’:

    contains, ends_with, everything, matches, num_range, one_of,
    starts_with

Error: Unknown TZ UTC
In addition: Warning message:
In OlsonNames() : no Olson database found
Execution halted
~~~

