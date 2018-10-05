## Getting Started

Please complete the following steps to get started as a contributor.

1. You will need an account on a Linux computer. If you a student in the Piccolo lab, you can use the ```daniel``` computer for this (talk to me if you need access). Or you can use the Supercomputer. 

2. If you haven't already done so, create a [GitHub](https://github.com) account.

3. Log in to the Linux computer. If you haven't already done so, you'll need to generate an SSH key.

    A. At the command line, enter the following command:

    ```
    ssh-keygen -t rsa
    ```

    B. When it asks you to "Enter a file in which to save the key," press Enter. This uses the default file location.

    C. When it asks you to enter a passphrase, press Enter (twice).

    D. Now there should be a file at ~/.ssh/id_rsa.pub. This is your public key and enables you to connect from Linux to GitHub without a password. Enter the following command to display the contents of this file. Then copy the output to your clipboard.

    ```
    cat ~/.ssh/id_rsa.pub
    ```
  
    E. Go to https://github.com/settings/keys. This should display the SSH keys that are currently specified for your GitHub account. Click on "New SSH key", enter a title, paste the public key from your clipboard, and click on "Add SSH key."

### Processing a new dataset

For each new dataset that you would like to prepare, you will need to complete the following steps. [Here](https://github.com/srp33/WishBuilder/tree/master/ICGC_BRCA-US_exp_seq/) you can see an example set of scripts to process a dataset.

1. "Fork" the WishBuilder GitHub repository by clicking on "Fork" (upper right hand corner of the webpage). You will make all of your future changes for this dataset on this forked repository.

2. Find your repository URL by navigating to your new forked repository and clicking on "Clone or download". Your repository URL should look something like this:

    ```
    git@github.com:glenrs/WishBuilder.git
    ```

3. At the command line, clone your forked WishBuilder repository using the URL you just retrieved. Then ```cd``` into the WishBuilder directory. Below is an example:

    ```
    git clone git@github.com:glenrs/WishBuilder.git
    cd WishBuilder
    ```

4. This directory is your own separate version of WishBuilder, so you can make changes without affecting the main WishBuilder project.

5. Create a new branch on your forked reposity. Replace `<new-branch-name>` with a unique ID for the dataset you are working with.

    ```
    git checkout -b <new-branch-name>
    ```

6. Create a new directory within your branched repository; the name of this directory should be the same ID you used for the branch name.

7. `cd` into this new directory.

8. Write a bash script called `install.sh` that installs any software needed to parse the data. In most cases, this script will be empty because WishBuilder already has installed commonly used software, such as the Python and R runtime environments.

9. Write a bash script called `download.sh` that downloads the data file(s) from the source location to the current directory.

10. In most cases, you will want to split the data into different categories. For example, some of your data might be "Clinical" data and the rest of your data might be "Gene Expression" data. Using a text editor, open the data files that you will be parsing and decide which categories you would like to use. For each of these categories, you will need to use a text editor to create a test file called `test_<Category>.tsv`, but you will replace `<Category>` with the actual category name. So if it were Clinical data, the name of this file would be `test_Clinical.tsv`. [Below](#test-files) you can learn about the purpose of these files and how they should be structured.

11. Write a bash script called `parse.sh`. This script should parse the downloaded data file(s) and reformat the data (as needed) into the output format described [below](#output-file-format). In most cases, `parse.sh` will invoke script(s) written in Python or R. The names of these output files should use this format: `<Category>.tsv.gz` (replace `<Category>` with the actual category name.

12. Create a bash script called `cleanup.sh`. Within that script, use Linux commands to delete the data files and any other non-script files after they have been generated using `parse.sh`. This will help ensure that *only* script files are committed to GitHub. **Please do not commit (see next step) any *data files* to GitHub.**

13. Create a [Markdown-formatted](https://guides.github.com/features/mastering-markdown/) file called `description.md` that provides a brief description of the dataset. The first line of the file should be a 2nd-level header (starting with `## `) that briefly describes the dataset. The rest of the file should contain additional details about the dataset, including its source, what the data can be used for, etc. Please separate each paragraph with 2 newline characters. You can see an example [here](https://github.com/srp33/WishBuilder/blob/master/ICGC_BRCA-US_exp_seq/).

14. Create a [YAML-formatted](https://en.wikipedia.org/wiki/YAML) file called `config.yaml` that indicates additional information about the data set. Below is an example of how this file should look. The `title` is a user-friendly description of the dataset. This title will be displayed on the Geney web site. The `featureDescription` indicates what type of biological entity is being profiled. In the example below, gene-expression levels are being profiled, so we put the word "gene" (in lower case). Alternatively, if transcript or protein levels were being profiled, we might put "transcript" or "protein," respectively. Specifying these values enables us to customize the way datasets are described in Geney. The `featureDescriptionPlural` is a plural version of `featureDescription`; it is not always easy for a computer to determine the plural version of a singular noun, so we specify it explicitly.

    ```
    title: Predicting Relapse in Favorable Histology Wilms Tumor Using Gene Expression
    featureDescription: gene
    featureDescriptionPlural: genes
    ```

15. Add, commit, and push your changes to the branch that you created earlier. Follow the example below, but replace `<message>` with a brief message that describes the work you have done, and replace `<new-branch-name>` with the name of the branch you created previously.

    ```
    git add --all
    git commit -m "<message>"
    git push origin <new-branch-name>
    ```

16. Go [here](https://github.com/srp33/WishBuilder/compare?expand=1) to create a GitHub pull request. Before navigating to any branches, please click on "compare accross forks". Put "srp33/Wishbuilder" as the base fork and "master" as the base branch and your repository as the head for and your new branch as the compare branch. Click on "Create pull request". We will check to make sure your code is working properly. If it is, we will integrate your code into the master branch of the WishBuilder repository.

## Notes

- Python (version 3.6.3) and R (version 3.4.4) are installed within the environment used to test WishBuilder scripts. The environment also includes popular Python modules are R packages. If you would like to know whether a particular module/package is installed, or if you would like to request an additional module/package, please let us know by submitting an [issue](https://github.com/srp33/WishBuilder/issues).
- If you create temporary files, please store these within the same directory as your scripts (or a subdirectory). This will ensure that everything needed to process each dataset is contained within the same location.
- When you specify file or directory paths in your scripts, please use *relative* rather than *absolute* paths.
- For additional information about creating branches and pull requests, read [this](https://gist.github.com/Chaser324/ce0505fbed06b947d962).

## Output File Format

Your scripts should produce at least one tab-delimited text files containing parsed data. The table below illustrates how these data files should be structured. All of the sample names should be unique. All of the column names should be unique. The name of the first column should be "Sample".

| Sample       | Gene1 | Gene2 | Gene3 | ... |
|--------------|---------------- |---------------- |---------------- |-----|
| TCGA-01-1234 | 5.23            | 5.11            | 7.42            | ... |
| TCGA-02-5678 | 4.67            | 9.82            | -0.98           | ... |
| ...          | ...             | ...             | ...             | ...   |

 These files should be gzipped, and the names of these files should reflect the data stored in them. For example, you might have one file containing clinical data that you call `Clinical.tsv.gz`, and you might have another file called `Gene_Expression.tsv.gz` that contains gene-expression data for the same patients. The sample identifiers used in these files should overlap with each other.

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

You should create one test file for each data file that your scripts generate. For example, if your scripts generate data files called `Clinical.tsv.gz` and `Gene_Expression.tsv.gz`, you will need to create test files called `test_Clinical.tsv` and `test_Gene_Expression.tsv`. Each of these files should have at least 8 lines of data (not including the header). These lines should contain data values that you have extracted by hand from the input file(s). Please include data values for at least two different samples and at least two different variables in each input file. Include at least one sample/variable from the beginning of each file and at least one from the ending of each file. Also include as least one sample/variable from the far-left side of each input file and at least one from the far-right side of each input file. **Create these test files based on what you see in the original data files, not in the output files that your code generates.**
