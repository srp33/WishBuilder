import sys, gzip

inFilePath = "donor.all_projects.tsv.gz"
outFilePath = "data.tsv.gz"

# This dataset is pretty straightforward. Already in correct format. Just left out study_donor_involved_in and submitted_donor_id columns and renamed first column.

columnsOfInterest = ["icgc_donor_id", "project_code", "donor_sex", "donor_vital_status", "disease_status_last_followup", "donor_relapse_type", "donor_age_at_diagnosis", "donor_age_at_enrollment", "donor_age_at_last_followup", "donor_relapse_interval", "donor_diagnosis_icd10", "donor_tumour_staging_system_at_diagnosis", "donor_tumour_stage_at_diagnosis", "donor_tumour_stage_at_diagnosis_supplemental", "donor_survival_time", "donor_interval_of_last_followup", "prior_malignancy", "cancer_type_prior_malignancy", "cancer_history_first_degree_relative"]

with gzip.open(inFilePath, 'r') as inFile:
    with gzip.open(outFilePath, 'wb') as outFile:
        inHeaderItems = inFile.readline().decode().rstrip("\n").split("\t")

        indicesOfInterest = [i for i in range(len(inHeaderItems)) if inHeaderItems[i] in columnsOfInterest]
        outHeaderItems = [inHeaderItems[i] for i in indicesOfInterest]
        outHeaderItems[0] = "Sample"
        outLine = "\t".join(outHeaderItems) + "\n"
        outFile.write(outLine.encode())

        for line in inFile:
            lineItems = line.decode().rstrip("\n").split("\t")
            lineItems = [lineItems[i] for i in indicesOfInterest]
            outLine = "\t".join(lineItems) + "\n"
            outFile.write(outLine.encode())
