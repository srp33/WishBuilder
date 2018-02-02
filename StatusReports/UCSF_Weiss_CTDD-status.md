<h1><center>UCSF_Weiss_CTDD</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Feb 01, 18 17:02PM MST</center>


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

Executing download.sh: 

&#10060;	download.sh returned an error:
~~~bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  9 1838k    9  174k    0     0   129k      0  0:00:14  0:00:01  0:00:13  129k
 68 1838k   68 1260k    0     0   539k      0  0:00:03  0:00:02  0:00:01  539k
100 1838k  100 1838k    0     0   643k      0  0:00:02  0:00:02 --:--:--  643k
./download.sh: line 21: unzip: command not found
~~~

