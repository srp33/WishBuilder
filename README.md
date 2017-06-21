# WishBuilder

## Prepping Data for Geney

Fortunately, many valuable biology-related datasets are publicly available on the Web. Commonly, a researcher wants to filter a dataset to include biological samples that meet specific criteria and perhaps to examine data for a few specific entities (genes, proteins, etc.). Unfortunately, researchers often have a difficult time working with these datasets due to their large size or because they are stored in a wide variety of formats. Accordingly, computational skills are required to _extract_ such data and _transform_ it into a format that can be _loaded_ easily into analytical tools. However, many biologists lack the expertise to _extract_, _transform_, and _load_ (ETL) such data.

To address this problem, the Piccolo lab is developing _Geney_, a Web-based tool that will enable researchers to query such datasets in a consistent and easy manner. In addition to Geney, we are developing _WishBuilder_ (name subject to change), a system that enables datasets to be imported into Geney, irrespective of the format in which the data were originally stored. This system downloads data from public Web servers, reformats the data, and stores it in a consistent, queryable format. To facilitate this process, we are asking for help from students to write scripts to prepare such datasets. The more datasets we prepare, the more useful Geney will be!

## Getting Started

Please complete the following steps to get started.

- You will need an active account on the BYU Supercomputer. If you don't currently have an active account, please go to https://marylou.byu.edu and click on "Request an Account." Read the information on that page. Then request an account, listing me as a mentor. When it asks what type of work you plan to perform, explain this research project briefly. Indicate that you will execute custom Python and/or R scripts, that you expect to execute only single-core jobs, and that these jobs will typically require 1-4 GB of memory per job.
- If you haven't already done so, create a [GitHub](https://github.com/) account.

## Preparing a Dataset

Please complete the following steps for each data set. Please talk to me if you have any questions or run into any problems.

1. Examine the list of datasets below and identify one that you would like to work with.
2. Put your name where it says "Status." Put **"IN PROGRESS" and the current date** next to your name.
3. Log in to the Supercomputer. Then clone the WishBuilder git repository:

  ```
  git clone https://github.com/srp33/WishBuilder.git
  cd WishBuilder
  ```

4. Or if you previously cloned the WishBuilder git repository, make sure it is up to date:

  ```
  git pull origin master
  ```

5. Create a new branch on your copy of the git repository (see below). Replace `<new-branch-name>` with the ID of the dataset you are working with.

  ```
  git checkout -b <new-branch-name>
  ```

6. Create a new directory within your branched repository; the name of this directory should also be the ID of the dataset you are working with. Then `cd` into the new directory.
7. Write a bash script called `download.sh` that downloads the data file(s) from the source location to the current directory. You can see an example [here](https://github.com/srp33/WishBuilder/tree/master/ICGC_Donor_Clinical).
8. Create a file called `.gitignore`. Within that file, list the name(s) of the file(s) that were downloaded. You can learn more about `.gitignore` files [here](https://help.github.com/articles/ignoring-files/).
9. Open the data file(s) in a text editor and examine them to understand how they are structured. (If the data file is too large for a text editor, use commands such as head, tail, and less to examine the file.)
10. Using a text editor, create a file called `testdata.tsv`. [Below](#datasets) you can learn about the purpose of this file and how it should be structured. You can see an example [here](https://github.com/srp33/WishBuilder/tree/master/ICGC_Donor_Clinical).
11. Write a bash script called `parse.sh`. You can see an example [here](https://github.com/srp33/WishBuilder/tree/master/ICGC_Donor_Clinical). This script should parse the data file(s) and reformat the data (as needed) into the output format described below. In most cases, `parse.sh` will invoke other script(s) written in Python or R. The name of the output file must be `data.tsv.gz`. _Recommendation: work with a smaller version of the data file(s) initially so it is easier to test._
12. Compare `data.tsv.gz` and `testdata.tsv` and make sure the data values were parsed correctly.
13. Add a line to `.gitignore` for `data.tsv.gz`.
14. Add, commit, and push your changes to the GitHub branch that you created earlier. Replace `<message>` with a brief messages that describes the work you have done. Replace `<new-branch-name>` with the name of the branch you created previously.

  ```
  git add --all
  git commit -m "<message>"
  git push origin <new-branch-name>
  ```

15. Go [here](https://github.com/srp33/WishBuilder/compare?expand=1) to create a GitHub pull request. Put "master" as the base branch and your new branch as the compare branch. Click on "Create pull request".
16. Below, where it says, "Status," put **"READY FOR TESTING" and the current date** next to your name.
17. Send me an email indicating that your dataset is ready for testing.

## Notes

- Python 3.5 is installed on the Supercomputer; use `module load python/3/5`.
- R is also installed on the Supercomputer; use `module load r/3/3`.
- As you write your parsing scripts, please make sure they use no more than 4 GB of memory. For larger datasets, avoid reading the whole file into memory. You can test your parse.sh script on the Supercomputer. But **please request no more than 4 GB of memory**.
- You can download files via the interactive nodes of the Supercomputer but not via the compute nodes. The latter do not have access to the Web.

## Test files

We will use your test file to verify that your scripts are working properly. We will execute your scripts and verify that the data values produced by your scripts match the data values in the test file (even though the format of these files will be different). You will need to create the test file using a text editor (see below).

The following table shows how your test file should be structured. This file should be tab delimited and should contain a header line with column names as shown below. This file should have at least 8 lines in it (not including the header). These lines should contain data values that you have extracted from the input file(s) for your dataset. Please include data values for at least two different samples and four different variables in each input file. Include at least one sample/variable from the beginning of each file and at least one from the ending of each file. Also include as least one sample/variable from the far left of each file and the far-right side of each file.

| Sample       | Variable | Value |
|--------------|----------|-------|
| TCGA-01-1234 | Age      | 34    |
| TCGA-01-1234 | Sex      | M     |
| TCGA-01-1234 | BRCA1    | 1     |
| TCGA-01-1234 | BRCA2    | 0     |
| TCGA-02-5678 | Age      | 92    |
| TCGA-02-5678 | Sex      | F     |
| TCGA-02-5678 | BRCA1    | 0     |
| TCGA-02-5678 | BRCA2    | 1     |
| ...          | ...      | ...   |

## Output file format

Your scripts should produce a single, tab-delimited text file that follows the structure shown below. Geney will import this data file.

All of the sample names should be unique. All of the column names should be unique. The name of the first column should be "Sample". This file should be gzipped and should be called `data.tsv.gz`.

| Sample       | Age | Sex | BRCA1 | BRCA2 | ... |
|--------------|-----|-----|-------|-------|-----|
| TCGA-01-1234 | 34  | M   | 1     | 0     | ... |
| TCGA-02-5678 | 92  | F   | 0     | 1     | ... |
| ...          | ... | ... | ...   | ...   | ... |

## <a name="datasets"></a>Datasets

### Cancer Cell Line Encyclopedia – mRNA isoform

Status: Maddy IN PROGRESS 6/16/17  
ID: CCLE_mRNA_isoform_kallisto_Tatlow  
Download URL: https://files.osf.io/v1/resources/gqrz9/providers/osfstorage/5783dacd9ad5a101f66b5daa?action=download&version=1&direct  
Notes:

- Each column (except the first) contains data for a single cell line (sample).
- Each row contains data for a specific transcript.
- The first column contains multiple identifiers separated by vertical bars (|). Please parse out the first identifier (for example, ENST00000000233.9), use that, and discard the rest.
- After we get this done, we will want to parse the clinical data as well. But let's deal with that later.

Sources:

- https://www.nature.com/articles/srep39259
- https://www.ncbi.nlm.nih.gov/pubmed/22460905

### GSE10320 - Predicting Relapse in Favorable Histology Wilms Tumor Using Gene Expression
Status:  
ID: GSE10320_SCAN  
Download URLs:

- https://files.osf.io/v1/resources/ssk3t/providers/osfstorage/594047f09ad5a100458248cf?action=download&version=1&direct
- https://files.osf.io/v1/resources/ssk3t/providers/osfstorage/592605289ad5a1024f3e59c8?action=download&version=1&direct

Notes:

- This one should be pretty easy because the data files are already structured how they need to be structured. But the two data files will need to be merged. The Class variable should be the first column in the output file.

Source:

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE10320


### GSE62944

Status: Jake Hogan IN PROGRESS 6/17/17  
ID: GSE62944_Tumor_TPM  
Download URLs:

- https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz
- https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FNormal%5FCancerType%5FSamples%2Etxt%2Egz
- https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file (TAR file- 5.9 gb)

Notes:

- Jake, please fill in any details here that you think are relevant.

Source: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE62944
