# WishBuilder

## Prepping Data for Geney

Fortunately, thousands of biology-related datasets are publicly available on the Web. Commonly, researchers want to filter individual datasets to include biological samples that meet specific criteria and to examine data for a few variables (e.g., genes, proteins) at a time. Unfortunately, researchers often have a difficult time performing these tasks because many datasets are large in size, and they are stored in a wide variety of formats.

To address this problem, the Piccolo lab is developing _Geney_, a Web-based tool that will enable researchers to query such datasets in a consistent and easy manner. In addition to _Geney_, we are developing _WishBuilder_, a system that enables datasets to be imported into _Geney_, irrespective of the format in which the data were originally stored. This system downloads data from public Web servers, reformats the data, and stores it in a consistent, queryable format. To facilitate this process, we are asking for help from BYU students to write computer scripts for preparing the data. The more datasets we prepare, the more useful Geney will be!

## Getting Started

Please complete the following steps to get started as a contributor.

1. You will need an account on the BYU Supercomputer. If you don't currently have an active account, please go to https://marylou.byu.edu and click on "Request an Account." Read the information on that page. Then request an account, listing me as a mentor. When it asks what type of work you plan to perform, explain briefly that you will execute custom Python scripts, that you expect to execute only single-core jobs, and that these jobs will typically require 1-16 GB of memory per job.

2. If you haven't already done so, create a [GitHub](https://github.com) account.

3. Send an email to me with your GitHub user ID and request to be added as a contributor to the WishBuilder repository.

4. **After you receive access to the Supercomputer**, log in to it. At the command line, enter the following commands (but substitute your actual email address where it says `your_email@example.com`):

  ```
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```

5. When it asks you to "Enter a file in which to save the key," press Enter. This uses the default file location.

6. When it asks you to enter a passphrase, press Enter (twice).

7. Now there should be a file at ~/.ssh/id_rsa.pub. Enter the following command to display the contents of this file. Then copy the output to your clipboard. This is your public key and enables you to connect from Linux to GitHub without a password.

  ```
  cat ~/.ssh/id_rsa.pub
  ```
  
8. Go to https://github.com/settings/keys. This should display the SSH keys that are currently specified for your GitHub account. Click on "New SSH key", enter a Title (maybe "FSL"), paste the public key from your clipboard, and click on "Add SSH key."


## Preparing a Dataset

Please complete the following steps for each dataset that you prepare. Let me know if you have any questions or run into any problems.

1. Examine the list of [open issues](https://github.com/srp33/WishBuilder/issues). Each "issue" represents a dataset that needs to be prepared. Identify one issue that you would like to work on (and that nobody else is currently working on).

2. Send an email to me indicating which issue you would like to work on.

3. At the command line on the Supercomputer, clone the WishBuilder git repository:

  ```
  git clone https://github.com/srp33/WishBuilder.git
  cd WishBuilder
  ```

4. Or if you previously cloned the WishBuilder git repository, make sure it is up to date:

  ```
  git pull origin master
  ```

5. Create a new branch on your copy of the git repository (see below). Replace `<new-branch-name>` with the ID of the dataset you are working with (the ID will be listed under the issue).

  ```
  git checkout -b <new-branch-name>
  ```

6. Create a new directory within your branched repository; the name of this directory should also be the ID of the dataset you are working with.

7. Now `cd` into the new directory.

8. Write a bash script called `download.sh` that downloads the data file(s) from the source location to the current directory. You can see an example [here](https://github.com/srp33/WishBuilder/tree/master/ICGC_Donor_Clinical).

9. Create a file called `.gitignore`. Within that file, list the name(s) of the file(s) that were downloaded. You can learn more about `.gitignore` files [here](https://help.github.com/articles/ignoring-files/).

10. Open the data file(s) in a text editor and examine them to understand how they are structured. (If the data file is too large for a text editor, use commands such as head, tail, and less to examine the file.)

11. Using a text editor, create test files called `test_metadata.tsv` and `test_data.tsv`. [Below](#test-files) you can learn about the purpose of these files and how they should be structured. You can see examples [here](https://github.com/srp33/WishBuilder/tree/master/ICGC_Donor_Clinical).

12. Write a bash script called `parse.sh`. This script should parse the downloaded data file(s) and reformat the data (as needed) into the output format described [below](#output-file-format). In most cases, `parse.sh` will invoke script(s) written in Python. The name of the output files *must* be `metadata.tsv.gz` and `data.tsv.gz`. _Recommendation: work with a smaller version of the data file(s) initially, so it is easier to test._ You can see an example [here](https://github.com/srp33/WishBuilder/tree/master/ICGC_Donor_Clinical).

13. Write a bash script called `install.sh` that installs any software that are necessary to execute `parse.sh`. If no extra software must be installed, it can be blank. You can see an example [here](https://github.com/srp33/WishBuilder/tree/master/ICGC_Donor_Clinical).

14. Compare `metadata.tsv.gz` against `test_metadata.tsv`. Make sure the metadata values were parsed correctly.

15. Compare `data.tsv.gz` against `test_data.tsv`. Make sure the data values were parsed correctly.

16. Add a line to `.gitignore` for `metadata.tsv.gz` and `data.tsv.gz`.

17. Add, commit, and push your changes to the branch that you created earlier. Replace `<message>` with a brief messages that describes the work you have done. Replace `<new-branch-name>` with the name of the branch you created previously.

  ```
  git add --all
  git commit -m "<message>"
  git push origin <new-branch-name>
  ```

18. Go [here](https://github.com/srp33/WishBuilder/compare?expand=1) to create a GitHub pull request. Put "master" as the base branch and your new branch as the compare branch. Click on "Create pull request". We will then check to make sure your code is working properly. If it is, we will integrate your code into the WishBuilder repository.

## Notes

- Python 3.5 is installed on the Supercomputer; use `module load python/3/5`.
- R is also installed on the Supercomputer; use `module load r/3/3`.
- As you write your parsing scripts, please make sure they use no more than 4 GB of memory.
- For larger datasets, avoid reading the whole file into memory. You can test your parse.sh script on the Supercomputer. But **please request no more than 4 GB of memory**.
- You can download files when you are executing code on the *interactive* nodes of the Supercomputer. But the *compute* nodes do not have access to the Internet.
- If you create temporary files, please store these within the same directory as your scripts (or a subdirectory). This will ensure that everything needed to process each dataset is contained within the same location.
- When you specify file or directory paths in your scripts, please use *relative* rather than *absolute* paths.

## Test files

We will use your test files to verify that your scripts are working properly. We will execute your scripts and then verify that the data values produced by your scripts match the data values in the test files, even though the format of these files will be different. You will need to create the test files using a text editor.

The following table shows how your test files should be structured. The files should be tab delimited and should contain a header line with column names as shown below.

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

You should create two test files: `test_metadata.tsv` and `test_data.tsv`. The first (`test_metadata.tsv`) should contain metadata values as described in the GitHub issue for your dataset. The second (`test_data.tsv`) should contain regular data values as described in the GitHub issue.

Each of these files should have at least 8 lines of data (not including the header). These lines should contain data values that you have extracted by hand from the input file(s). Please include data values for at least two different samples and four different variables in each input file. Include at least one sample/variable from the beginning of each file and at least one from the ending of each file. Also include as least one sample/variable from the far left of each file and the far-right side of each file.

## Output file format

Your scripts should produce two tab-delimited text files: `metadata.tsv.gz` and `data.tsv.gz` (see below). Geney will import these data files.

`metadata.tsv.gz` should be structured the same as `test_metadata.tsv`, except that it should contain all metadata values and should be gzipped.

The table below illustrates how `data.tsv.gz` should be structured. All of the sample names should be unique. All of the column names should be unique. The name of the first column should be "Sample". This file should be gzipped.

| Sample       | Age | Sex | BRCA1 | BRCA2 | ... |
|--------------|-----|-----|-------|-------|-----|
| TCGA-01-1234 | 34  | M   | 1     | 0     | ... |
| TCGA-02-5678 | 92  | F   | 0     | 1     | ... |
| ...          | ... | ... | ...   | ...   | ... |

