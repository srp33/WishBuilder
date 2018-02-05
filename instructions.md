## Getting Started

Please complete the following steps to get started as a contributor.

1. You will need an account on the BYU Supercomputer. If you don't currently have an active account, please go to https://marylou.byu.edu and click on "Request an Account." Read the information on that page. Then request an account, listing me as a mentor. When it asks what type of work you plan to perform, explain briefly that you will execute custom Python scripts, that you expect to execute only single-core jobs, and that these jobs will typically require 1-16 GB of memory per job.

2. If you haven't already done so, create a [GitHub](https://github.com) account.

3. **After you receive access to the Supercomputer**, log in to it. At the command line, enter the following commands (but substitute your actual email address where it says `your_email@example.com`):

  ```
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```

4. When it asks you to "Enter a file in which to save the key," press Enter. This uses the default file location.

5. When it asks you to enter a passphrase, press Enter (twice).

6. Now there should be a file at ~/.ssh/id_rsa.pub. Enter the following command to display the contents of this file. Then copy the output to your clipboard. This is your public key and enables you to connect from Linux to GitHub without a password.

  ```
  cat ~/.ssh/id_rsa.pub
  ```
  
7. Go to https://github.com/settings/keys. This should display the SSH keys that are currently specified for your GitHub account. Click on "New SSH key", enter a Title (maybe "FSL"), paste the public key from your clipboard, and click on "Add SSH key."

8. After you have set up your ssh key so that GitHub can recognize your pull requests please return to this repository and fork this repository by clicking on "Fork" (upper right hand corner of the webpage). Please make all your pull requests from your forked repository.

## Preparing a Dataset

Please complete the following steps for each dataset that you prepare. Let me know if you have any questions or run into any problems.

1. Examine the list of [open issues](https://github.com/srp33/WishBuilder/issues). Each "issue" represents a dataset that needs to be prepared. Identify one issue that you would like to work on (and that nobody else is currently working on).

2. Send an email to me indicating which issue you would like to work on.

3. Please find your repository api by navigating to your new forked repository and clicking on "clone or download". Your repository api should look something like this:

  ```
  git@github.com:glenrs/WishBuilder.git
  ```

3. At the command line on the Supercomputer, clone your forked WishBuilder git repository using this api you just retrieved :

  ```
  git clone <your-forked-repository-api>
  cd WishBuilder
  ```

4. Or if you previously cloned the your forked WishBuilder git repository, make sure it is up to date:

  ```
  git pull origin master
  ```

5. Create a new branch on your copy of the git repository (see below). Replace `<new-branch-name>` with the ID of the dataset you are working with (the ID will be listed under the issue).

  ```
  git checkout -b <new-branch-name>
  ```

6. Create a new directory within your branched repository; the name of this directory should also be the ID of the dataset you are working with.

7. Now `cd` into the new directory.

8. Write a bash script called `download.sh` that downloads the data file(s) from the source location to the current directory. You can see an example [here](https://github.com/srp33/WishBuilder/blob/master/ICGC_BRCA-US_exp_seq/).

9. Open the data file(s) in a text editor and examine them to understand how they are structured. (If the data file is too large for a text editor, use commands such as head, tail, and less to examine the file.)

10. Using a text editor, create test files called `test_metadata.tsv` and `test_data.tsv`. [Below](#test-files) you can learn about the purpose of these files and how they should be structured. You can see examples [here](https://github.com/srp33/WishBuilder/blob/master/ICGC_BRCA-US_exp_seq/).

11. Write a bash script called `parse.sh`. This script should parse the downloaded data file(s) and reformat the data (as needed) into the output format described [below](#output-file-format). In most cases, `parse.sh` will invoke script(s) written in Python. The name of the output files *must* be `metadata.tsv.gz` and `data.tsv.gz`. _Recommendation: work with a smaller version of the data file(s) initially, so it is easier to test._ You can see an example [here](https://github.com/srp33/WishBuilder/blob/master/ICGC_BRCA-US_exp_seq/).

12. Write a bash script called `install.sh` that installs any software that are necessary to execute `parse.sh`. If no extra software must be installed, it can be blank. You can see an example [here](https://github.com/srp33/WishBuilder/blob/master/ICGC_BRCA-US_exp_seq/).

13. Compare `metadata.tsv.gz` against `test_metadata.tsv`. Make sure the metadata values were parsed correctly.

14. Compare `data.tsv.gz` against `test_data.tsv`. Make sure the data values were parsed correctly.

15. Create a bash script called `cleanup.sh`. Within that script, use the `rm` command to delete `metadata.tsv.gz`, `data.tsv.gz`, and any other non-script files. **Please do not commit (see next step) any *data files* to GitHub.**

16. Create a [Markdown-formatted](https://guides.github.com/features/mastering-markdown/) file called `description.md` that provides a brief description of the dataset. The first line of the file should be a 2nd-level header (starting with `## `) that briefly describes the dataset. The rest of the file should contain additional details about the dataset, including its source, what the data can be used for, etc. Please separate each paragraph with 2 newline characters. You can see an example [here](https://github.com/srp33/WishBuilder/blob/master/ICGC_BRCA-US_exp_seq/).

17. Create a [YAML-formatted](https://en.wikipedia.org/wiki/YAML) file called `config.yaml` that indicates additional information about the data set. Below is an example of how this file should look. The `title` is a user-friendly description of the dataset. This title will be displayed on the Geney web site. The `featureDescription` indicates what type of biological entity is being profiled in the "data" (not metadata). In the example below, gene-expression levels are being profiled, so we put the word "gene" (in lower case). Alternatively, if transcript or protein levels were being profiled, we might put "transcript" or "protein," respectively. Specifying these values enables us to customize the way each dataset is described in Geney. The `featureDescriptionPlural` is a plural version of `featureDescription`; it is not always easy for a computer to determine the plural version of a singular noun, so we specify it explicitly.

  ```
  title: Predicting Relapse in Favorable Histology Wilms Tumor Using Gene Expression
  featureDescription: gene
  featureDescriptionPlural: genes
  ```

18. Add, commit, and push your changes to the branch that you created earlier. Replace `<message>` with a brief messages that describes the work you have done. Replace `<new-branch-name>` with the name of the branch you created previously.

  ```
  git add --all
  git commit -m "<message>"
  git push origin <new-branch-name>
  ```

19. Go [here](https://github.com/srp33/WishBuilder/compare?expand=1) to create a GitHub pull request. Before navigating to any branches, please click on "compare accross forks". Put "srp33/Wishbuilder" as the base fork and "master" as the base branch and your repository as the head for and your new branch as the compare branch. Click on "Create pull request". We will check to make sure your code is working properly. If it is, we will integrate your code into the master branch of the WishBuilder repository. You can check the status [here](https://srp33.github.io/WishBuilder/docs/dataSets). It may take hours (or even days) to finish processing, depending on the size of your data. 

### Setting Up WishBuilder Dependencies

1. The container that will be running automated test scripts will require certain dependencies. We have created [this](https://github.com/glenrs/WishBuilderData/blob/master/ManagingWishBuilder/installWishBuilderDependencies.sh) script. Please run this script on the supercomputer. It will create a anaconda environment that will store all dependencies.

2. In order for you to easily use this environment you will need to add miniconda to your path on the supercomputer. Please open your .bash_profile in your root directory and add the following code:

```
export PATH=$PATH
PATH=~/Software/miniconda/bin:$PATH
export PATH
```

3. Your datset may require additional software to download, parse, and filter your dataset. You might wish to add these additional software packages to this package on the supercomputer and the container used for testing. You can easily install more software in this package on the supercomputer by opening the environment, and using the "conda install" function to easily install anything that is necessary:

```
  source activate WishBuilderDependencies 
  conda install -y -c bioconda r-sleuth
  conda install -y -c r r-xml=3.98_1.5
  conda install -y gcc
  Rscript installRPackages.R
  source deactivate WishBuilderDependencies
```

4. Before you submit, please comment out the environment. Remember this environment is created for the supercomputer and is not on the container. You can easily download the needed software without making the environment. 

```
  #source activate WishBuilderDependencies 
  conda install -y -c bioconda r-sleuth
  conda install -y -c r r-xml=3.98_1.5
  conda install -y gcc
  Rscript installRPackages.R
  #source deactivate WishBuilderDependencies
```

## Notes

- Python 3.5 is installed on the Supercomputer; use `module load python/3/5`.
- R is also installed on the Supercomputer; use `module load r/3/3`.
- As you write your parsing scripts, please make sure they use no more than 4 GB of memory.
- For larger datasets, avoid reading the whole file into memory. You can test your parse.sh script on the Supercomputer. But **please request no more than 4 GB of memory**.
- You can download files when you are executing code on the *interactive* nodes of the Supercomputer. But the *compute* nodes do not have access to the Internet.
- If you create temporary files, please store these within the same directory as your scripts (or a subdirectory). This will ensure that everything needed to process each dataset is contained within the same location.
- When you specify file or directory paths in your scripts, please use *relative* rather than *absolute* paths.

## Test Files

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

Each of these files should have at least 8 lines of data (not including the header). These lines should contain data values that you have extracted by hand from the input file(s). Please include data values for at least two different samples and at least two different variables in each input file. Include at least one sample/variable from the beginning of each file and at least one from the ending of each file. Also include as least one sample/variable from the far-left side of each input file and at least one from the far-right side of each input file.

## Output File Format

Your scripts should produce two tab-delimited text files: `metadata.tsv.gz` and `data.tsv.gz` (see below). Geney will import these data files.

`metadata.tsv.gz` should be structured the same as `test_metadata.tsv`, except that it should contain all metadata values and should be gzipped.

The table below illustrates how `data.tsv.gz` should be structured. All of the sample names should be unique. All of the column names should be unique. The name of the first column should be "Sample". This file should be gzipped.

| Sample       | Expressed_Gene1 | Expressed_Gene2 | Expressed_Gene3 | ... |
|--------------|---------------- |---------------- |---------------- |-----|
| TCGA-01-1234 | 5.23            | 5.11            | 7.42            | ... |
| TCGA-02-5678 | 4.67            | 9.82            | -0.98           | ... |
| ...          | ...             | ...             | ...             | ...   |

The sample identifiers listed in `metadata.tsv.gz` and `data.tsv.gz` should overlap with each other. Neither file should contain any sample identifier that is not listed in both files (all non-overlapping samples should be excluded from both files).
