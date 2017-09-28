import sys, gzip

inFilePath = "donor.BRCA-US.tsv.gz"
outFilePath = "metadata.tsv.gz"

# This dataset is pretty straightforward. It is already in the correct format. Just need to leave out certain columns and rename the first column.

columnsOfInterest = ["icgc_donor_id", "submitted_donor_id", "donor_sex", "donor_vital_status", "disease_status_last_followup", "donor_age_at_diagnosis", "donor_age_at_last_followup", "donor_survival_time", "interval_of_last_followup"]

with gzip.open(inFilePath, 'r') as inFile:
    with gzip.open(outFilePath, 'wb') as outFile:
        inHeaderItems = inFile.readline().decode().rstrip("\n").split("\t")

        indicesOfInterest = [i for i in range(len(inHeaderItems)) if inHeaderItems[i] in columnsOfInterest]

        # Extract the column names for the columns of interest
        outHeaderItems = [inHeaderItems[i] for i in indicesOfInterest]

        # Rename the first and second columns to specific names
        outHeaderItems[0] = "Sample"
        outHeaderItems[1] = "TCGA_ID"

        # Remove unnecessary prefix from any column names that have it
        outHeaderItems = [x.replace("donor_", "") for x in outHeaderItems]

        outLine = "\t".join(outHeaderItems) + "\n"
        outFile.write(outLine.encode())

        for line in inFile:
            lineItems = line.decode().rstrip("\n").split("\t")
            lineItems = [lineItems[i] for i in indicesOfInterest]
            outLine = "\t".join(lineItems) + "\n"
            outFile.write(outLine.encode())
