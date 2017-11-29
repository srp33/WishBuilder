<h1><center>LINCS_PhaseII_Level4</center></h1>
<h2><center> Status: In Progress </center></h2>


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
Traceback (most recent call last):
  File "parse.py", line 14, in <module>
    f = h5py.File(gctxFileName, "r")
  File "/app/WishBuilder/testDirectory/Software/miniconda/envs/lincs_env/lib/python2.7/site-packages/h5py/_hl/files.py", line 272, in __init__
    fid = make_fid(name, mode, userblock_size, fapl, swmr=swmr)
  File "/app/WishBuilder/testDirectory/Software/miniconda/envs/lincs_env/lib/python2.7/site-packages/h5py/_hl/files.py", line 92, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper (/home/ilan/minonda/conda-bld/work/h5py/_objects.c:2696)
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper (/home/ilan/minonda/conda-bld/work/h5py/_objects.c:2654)
  File "h5py/h5f.pyx", line 76, in h5py.h5f.open (/home/ilan/minonda/conda-bld/work/h5py/h5f.c:1942)
IOError: Unable to open file (Unable to open file: name = 'tmp/lincs_phaseii_level5.gctx', errno = 2, error message = 'no such file or directory', flags = 0, o_flags = 0)
~~~

