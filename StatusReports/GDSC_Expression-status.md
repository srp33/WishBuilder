<h1><center>GDSC_Expression</center></h1>

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

Executing parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Key Files:

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (83; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	CAL-120	|	DMS-114	|	CAL-51	|	H2869	|
|	---	|	---	|	---	|	---	|	---	|
|	ENSG00000000003	|	7.63202317146339	|	7.54867116637172	|	8.71233752103624	|	7.79714221650204	|
|	ENSG00000000005	|	2.96458512058924	|	2.77771614989839	|	2.6435077554121	|	2.8179230218265	|
|	ENSG00000000419	|	10.3795526353077	|	11.8073412488458	|	9.88073281995499	|	9.88347076381233	|
|	ENSG00000000457	|	3.61479404843988	|	4.066886747621	|	3.95622995046262	|	4.06370139098185	|

**Columns: 0 Rows: 1**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#10060;	OCI-AML5 is in data.tsv.gz column headers more than once

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	CAL-120	|	Site	|	breast	|
|	CAL-120	|	Histology	|	carcinoma	|
|	CAL-120	|	GDSC Tissue descriptor 1	|	breast	|
|	CAL-120	|	GDSC Tissue descriptor 2	|	breast	|

**Columns: 3 Rows: 2911164**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NU7441_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK-650394_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ACHP_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PS-341_MAX_CONC_MICROMOLAR" for all samples is the same ("0.02"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-204_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_HDAC-42_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KT-555_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Axitinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_rTRAIL_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Daraprim_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Targrexin_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YM-155_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IKK Inhibitor 3_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB590885_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AT-7519_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-270_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PHA 665752_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ AUY_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZ 628_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB-590885_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT-263_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PXD-101_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BAY-86-9766_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TGX221_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VP-16_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AP24534_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_FTI-277_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NSC-207895_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_UNC1215_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_EHT-1864_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CX-5461_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Asp-2689_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AP-24534_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Piplartine_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Etopophos_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Exelbine_MAX_CONC_MICROMOLAR" for all samples is the same ("0.064"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Kessar_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VX 702_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PI-103_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GDC0449_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT-888_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Targret_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Midostaurin_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-260_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GW-2580_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BI-2536_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PD173074_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Embelin_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CH 542802_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Entinostat_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Nexavar_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NSC-87877_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_EX 527_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_L01XC06_MAX_CONC_MICROMOLAR" for all samples is the same ("65.8"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Amuvatinib_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YK 4-279_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Ara-Cytidine_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_THZ-2-49_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CUDC-101_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Ro-508231_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMN-673_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB505124_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tretinoin_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIL8951_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Zynoplex_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MP 470_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS 754807_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_212631-79-3_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Chloridine_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XMD13-2_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CUDC 101_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Z-LLNle-CHO_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Seliciclib_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_JNK inhibitor 9l_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB-715992_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Z-L-Norleucine-CHO_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_WIKI-4_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BHG712_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_RDEA119_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MS-275_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VX-11e_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Anchusin_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF-4708671_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TO901317_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Quizartinib_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_S-Trityl-L-cysteine_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tyverb_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TL-1-85_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_STI-571_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bryostatin 1_MAX_CONC_MICROMOLAR" for all samples is the same ("0.008"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_vinorelbine tartrate_MAX_CONC_MICROMOLAR" for all samples is the same ("0.064"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SU-11248_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Elesclomol_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Trexall_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_944328-88-5_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Zolinza_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Octanoic acid_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Rubex_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_T0901317_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Piperlongumine_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Dimethyloxalylglcine_MAX_CONC_MICROMOLAR" for all samples is the same ("4000.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Sirolimus_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF-00562271_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Belinostat_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TG101348_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-127_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MLN-4924_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SGC0946_MAX_CONC_MICROMOLAR" for all samples is the same ("0.5"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_N1-(b-D-Ribofuranosyl)-5-aminoimidazole-4-carboxamide_MAX_CONC_MICROMOLAR" for all samples is the same ("2000.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_JW-7-52-1_MAX_CONC_MICROMOLAR" for all samples is the same ("1.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-128_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-345541_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-509744_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Rapamune_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-019_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMN 973_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_LLL cpd_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Xalkori_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_LY-188011_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-354825-03_MAX_CONC_MICROMOLAR" for all samples is the same ("1.28"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ERK5-IN-1_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CEP-701_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Emberine_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TO-901317_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_681640_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-111_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MK-0683_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Velban_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_WIKI 4_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Genentech Cpd 10_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_suberoylanilide hydroxamic acid_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB-505124_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSI 930 OSI930_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF-2341066_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AS601245_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Parthenolide_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_HG6-64-1_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Dabrafenib_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bleomycin_MAX_CONC_MICROMOLAR" for all samples is the same ("64.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PAC-1_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TW37_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Refametinib_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IPA 3_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_WH-4-023_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CC-5013_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_JNK Inhibitor VIII_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Cyclopamine_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Navitoclax_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Lenalidomide_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ASP-7487_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CGP 60474_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_FR-180204_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_5-Fluorouracil_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PKC412_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Soltamox_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KRN-951_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AMN 107_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CX5461_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZD7762_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IOX-2_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YK-4-279_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Cometriq_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Taxotere_MAX_CONC_MICROMOLAR" for all samples is the same ("0.0125"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MG-132_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Nolvadex_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Patupilone_MAX_CONC_MICROMOLAR" for all samples is the same ("0.032"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Mitomycin-C_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Rapamycin_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB216763_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Temozolomide_MAX_CONC_MICROMOLAR" for all samples is the same ("30.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BAY-613606_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tivozanib_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-013_MAX_CONC_MICROMOLAR" for all samples is the same ("1.28"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB-216763_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK-1904529A_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AMG 706_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BAY 43-9006_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YM155_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK 690693_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF 4708671_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Trametinib_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-907351_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AK176060_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZD8055_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Sunitinib Malate_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_JNJ-26854165_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PD-173074_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Arabinosyl Cytosine_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Nilotinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TPCA-1_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BX796_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YM201636_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PLX4720_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_A-443654_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Thapsigargin_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_WIKI4_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CP466722_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Temodal_MAX_CONC_MICROMOLAR" for all samples is the same ("30.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CYC-202_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Camptothecin_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GX15-070_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TAE684_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CP 466722_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PHA-665752_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Atralin_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZD0530_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Rheumatrex_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TW 37_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_DDE-28_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bortezomib_MAX_CONC_MICROMOLAR" for all samples is the same ("0.02"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Mytozytrex_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_WY-090217_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CCT018159_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tubastatin A_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZD-0530_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT888_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Pevonedistat_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Adriablastin_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ FK866_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_5Z-7-Oxozeaenol_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Docetaxel_MAX_CONC_MICROMOLAR" for all samples is the same ("0.0125"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Pazopanib_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CP-724714_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BX-796_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSI-774_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CX 5461_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Abitrexate_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CAY10603_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_EHT 1864_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bexarotenum_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_5-FU_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-754807_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Ponatinib_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PHA793887_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSI-906_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CGP-41251_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GTPL5238_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BAY-61-3606_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PLX-4720_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_HG-5-113-01_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_JW-7-24-1_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tozasertib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Motesanib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Gleevec_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Folex_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZD-8055_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Targretyn_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CMK_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PD-18435_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SL0101_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GX2580_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Luminespib_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AICAR_MAX_CONC_MICROMOLAR" for all samples is the same ("2000.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ICI-46474_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Abraxane_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Shikonin_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tgx 221_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Iressa_MAX_CONC_MICROMOLAR" for all samples is the same ("0.5"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NU-7432_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Temodar_MAX_CONC_MICROMOLAR" for all samples is the same ("30.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MPS-1-IN-1_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Saracatinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Obatoclax_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VER-52296,NVP-AUY922_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XMD15-27_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Sprycel_MAX_CONC_MICROMOLAR" for all samples is the same ("1.28"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XMD 8-92_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_EX-527_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SAR302503_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XAV-939_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NG-25_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZ628_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AR-42_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Epothilone B_MAX_CONC_MICROMOLAR" for all samples is the same ("0.032"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CDC-501_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BX-912_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CCI-779_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Daporinad_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Zarnestra_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-244_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tamoxifen_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PFI-1_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT 888_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AG-13736_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-236_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AC220_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PDK1 inhibitor AR-12_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bexarotene_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Doramapimod_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bayer IKKb inhibitor_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ZG-10_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Camptothecin-11_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Linsitinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Cetuximab_MAX_CONC_MICROMOLAR" for all samples is the same ("65.8"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_17-AAG_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Etoposide_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GX15-070MS_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ERK Inhibitor II_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK 1904529A_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK525762A_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VX11e_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_LAQ824_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSI-027_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK319347A_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ZD-1839_MAX_CONC_MICROMOLAR" for all samples is the same ("0.5"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_QS11_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_U-19920_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NSC207895_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IKK-3 inhibitor_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Sutent_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AC1L1GQE_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Gefitinib_MAX_CONC_MICROMOLAR" for all samples is the same ("0.5"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_LDP-341_MAX_CONC_MICROMOLAR" for all samples is the same ("0.02"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Crizotinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ASP-4130_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS754807_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Linifanib_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK1904529A_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tafinlar_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-181339-01_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_LG-100069_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Selisistat_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Alectinib_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Adriamycin_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Veliparib_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CP-358774_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TGX-221_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GW 441756_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Roscovitine_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_FR 180204_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-021_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XL-184_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-722782_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Doxil_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GW843682X (AN-13)_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_suberanilohydroxamic acid_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MP470_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT263_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Serdemetan_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Inlyta_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TAE-684_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Vepesid_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bleomycin (50 uM)_MAX_CONC_MICROMOLAR" for all samples is the same ("50.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_FR180204_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB-52334_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Sepantronium bromide_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XI-006_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XMD14-99_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Temsirolimus_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tykerb_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Iclusig_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB 216763_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Onxol_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PIK93_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IOX2_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Gemcitabine_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_A-770041_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_(5Z)-7-Oxozeaenol_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KU-55933_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NVP-TAE684_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Dasatinib_MAX_CONC_MICROMOLAR" for all samples is the same ("1.28"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TG-101348_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AUY922_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Vinblastine_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VX-680 VX 680 VX-68_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Erbitux_MAX_CONC_MICROMOLAR" for all samples is the same ("65.8"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CDK9-IN-1_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CP724714_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CI-1040_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_JQ12_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CDK9 inhibitor_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Revlimid_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_WHI-P97_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YM-201636_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AR 42_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VNLG/124_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SL-0101_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Obatoclax Mesylate_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bryostatin_MAX_CONC_MICROMOLAR" for all samples is the same ("0.008"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_JNK-9L_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK 650394_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_FK866_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MG 132_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NVP-TAE 684_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YM 155_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS-354825_MAX_CONC_MICROMOLAR" for all samples is the same ("1.28"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Cytarabine_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NPK76-II-72-1_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BMS345541_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_EpoB_MAX_CONC_MICROMOLAR" for all samples is the same ("0.032"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PHA-793887_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Votrient_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Imatinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_STF-62247_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SNX-2112_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_QL-VIII-58_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Dacinostat_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BIRB-796_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZD-7762_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AMG706_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_QL-XII-47_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BIX 02189_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_RG-1415_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BIX02189_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Fedratinib_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSI-930_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Avita_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Syk Inhibitor_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AICA Ribonucleotide_MAX_CONC_MICROMOLAR" for all samples is the same ("2000.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF-562271_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSU03012_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Gemzar_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT-869_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK1120212_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Lapatinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CCT007093_MAX_CONC_MICROMOLAR" for all samples is the same ("6.6"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Renova_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Doxorubicine_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tretin-X_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AR42_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_RO-3306_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tanespimycin_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CCT-018159_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Lestauritinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AG-14447_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SP-924_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PI103_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Gamma-Secretase Inhibitor 1_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NVP-LAQ824_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AC 220_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tritylcysteine_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Velcade_MAX_CONC_MICROMOLAR" for all samples is the same ("0.02"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IPA-3_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IOX 2_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_EIF-2alpha Inhibitor_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Ispinesib Mesylate_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Rucaparib_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB 505124_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF 2341066_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SAHA_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Paxene_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK2118436_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_YM 201636_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Eposin_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MLN4924_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CFMS receptor tyrosine kinase inhibitor_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VX-702_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-055_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KU55933_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GW441756_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_FH535_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bosulif_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-112_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Masitinib_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AG-14699_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_UNC-1215_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XMD11-85h_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSU-03012_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Cabozantinib_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PDK1 inhibitor 7_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Talazoparib_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_APO866_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SAR-302503_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Vorinostat_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Taxol_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-102_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AT7519_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_LL-Z1640-2_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SKI-606_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CGP-082996_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CH5424802_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SPM-924_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AV-951_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ZD-4054_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Vinorelbine_MAX_CONC_MICROMOLAR" for all samples is the same ("0.064"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tasigna_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF-01367338_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GNF-2_MAX_CONC_MICROMOLAR" for all samples is the same ("1.28"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Y-39983_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_STF62247_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NSC-26980_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Vismodegib_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZ-628_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Zibotentan_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NSC 87877_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Doxorubicin_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_QL-X-138_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PIK-93_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AG-014699_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Praxel_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MG132_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GW843682X_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB 52334_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AC-220_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BAY 869766_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_VX702_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CI 1040_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SCH 52365_MAX_CONC_MICROMOLAR" for all samples is the same ("30.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PD-184352_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Erlotinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Erivedge_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK690693_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SB52334_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-139_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ZD4054_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CP-466722_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ATRA_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NSC 83265_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK-690693_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-192_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PD 173074_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Navelbine_MAX_CONC_MICROMOLAR" for all samples is the same ("0.064"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CGP-60474_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MK 0457,MK-0457,MK-045_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Vesanoid_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_TW-37_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tipifarnib_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_A-1065-5_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AV 951_MAX_CONC_MICROMOLAR" for all samples is the same ("0.128"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT 869_MAX_CONC_MICROMOLAR" for all samples is the same ("1.024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PLX 4720_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Mekinist_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NVP-BHG712_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ABT 263_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PI 103_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AR-12_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AB1010_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XAV939_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-123_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_WZ-1-84_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Mitozytrex_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_C225_MAX_CONC_MICROMOLAR" for all samples is the same ("65.8"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF4708671_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Sorafenib_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZ-10353926_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PHA 793887_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CINK4_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IMC-225_MAX_CONC_MICROMOLAR" for all samples is the same ("65.8"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Salubrinal_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MMC_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NG25_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PXD101_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-266_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NVP-XAV939_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XMD8-92_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Paclitaxel_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1024"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_OSU 03012_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_NU-7741_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Embelic acid_MAX_CONC_MICROMOLAR" for all samples is the same ("32.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_DMOG_MAX_CONC_MICROMOLAR" for all samples is the same ("4000.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-135_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SL 0101-1_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AMG-706_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_benzoylstaurosporine_MAX_CONC_MICROMOLAR" for all samples is the same ("0.512"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Tarceva_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PHA665752_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KU-57788_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_LFM-A13_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_DBI_MAX_CONC_MICROMOLAR" for all samples is the same ("4000.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_284461-73-0_MAX_CONC_MICROMOLAR" for all samples is the same ("4.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_A-154475_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_1080622-86-1_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_STA-4783_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_ITK inhibitor_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Amethopterin_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GSK650394_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_R-1415_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Mitosol_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CGP60474_MAX_CONC_MICROMOLAR" for all samples is the same ("0.256"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Methotrexate_MAX_CONC_MICROMOLAR" for all samples is the same ("0.2"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_M-39831_MAX_CONC_MICROMOLAR" for all samples is the same ("30.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AL-39256_MAX_CONC_MICROMOLAR" for all samples is the same ("16.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AZD 7762_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_I-BET-762_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Alecensa_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Pyrimethamine_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_IMC-C225_MAX_CONC_MICROMOLAR" for all samples is the same ("65.8"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_QL-XII-61_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_GNF-PF-193_MAX_CONC_MICROMOLAR" for all samples is the same ("0.032"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Sunitinib_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XMD8-85_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PIK 93_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MP-470_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Bosutinib_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_SNX 2112_MAX_CONC_MICROMOLAR" for all samples is the same ("2.56"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_QL-XI-92_MAX_CONC_MICROMOLAR" for all samples is the same ("10.24"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_MLN 4924_MAX_CONC_MICROMOLAR" for all samples is the same ("1.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_PF2341066_MAX_CONC_MICROMOLAR" for all samples is the same ("2.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_AY-22989_MAX_CONC_MICROMOLAR" for all samples is the same ("0.1"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_BIRB 796_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_CCT 018159_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_RP-56976_MAX_CONC_MICROMOLAR" for all samples is the same ("0.0125"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Phenformin_MAX_CONC_MICROMOLAR" for all samples is the same ("4000.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_EPO906_MAX_CONC_MICROMOLAR" for all samples is the same ("0.032"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Masivet_MAX_CONC_MICROMOLAR" for all samples is the same ("20.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_XAV 939_MAX_CONC_MICROMOLAR" for all samples is the same ("5.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_HG-5-88-01_MAX_CONC_MICROMOLAR" for all samples is the same ("10.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_Targretin_MAX_CONC_MICROMOLAR" for all samples is the same ("8.0"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_KIN001-206_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

<p><font color="orange" size="+2">&#9888;	</font>The value for variable "Drug_HDAC inhibitor XV_MAX_CONC_MICROMOLAR" for all samples is the same ("5.12"). This variable has been removed from metadata.tsv.gz</p>

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

&#9989;	Row 13: Success

&#9989;	Row 14: Success

&#9989;	Row 15: Success

&#9989;	Row 16: Success

&#9989;	Row 17: Success

&#9989;	Row 18: Success

&#9989;	Row 19: Success

&#9989;	Row 20: Success

&#9989;	Row 21: Success

&#9989;	Row 22: Success

&#9989;	Row 23: Success

&#9989;	Row 24: Success

&#9989;	Row 25: Success

&#9989;	Row 26: Success

&#9989;	Row 27: Success

&#9989;	Row 28: Success

&#9989;	Row 29: Success

&#9989;	Row 30: Success

&#9989;	Row 31: Success

&#9989;	Row 32: Success

&#9989;	Row 33: Success

&#9989;	Row 34: Success

&#9989;	Row 35: Success

&#9989;	Row 36: Success

&#9989;	Row 37: Success

&#9989;	Row 38: Success

&#9989;	Row 39: Success

&#9989;	Row 40: Success

&#9989;	Row 41: Success

&#9989;	Row 42: Success

&#9989;	Row 43: Success

&#9989;	Row 44: Success

&#9989;	Row 45: Success

&#9989;	Row 46: Success

&#9989;	Row 47: Success

&#9989;	Row 48: Success

&#9989;	Row 49: Success

&#9989;	Row 50: Success

&#9989;	Row 51: Success

&#9989;	Row 52: Success

&#9989;	Row 53: Success

&#9989;	Row 54: Success

&#9989;	Row 55: Success

&#9989;	Row 56: Success

&#9989;	Row 57: Success

&#9989;	Row 58: Success

&#9989;	Row 59: Success

&#9989;	Row 60: Success

&#9989;	Row 61: Success

&#9989;	Row 62: Success

&#9989;	Row 63: Success

&#9989;	Row 64: Success

&#9989;	Row 65: Success

&#9989;	Row 66: Success

&#9989;	Row 67: Success

&#9989;	Row 68: Success

&#9989;	Row 69: Success

&#9989;	Row 70: Success

&#9989;	Row 71: Success

&#9989;	Row 72: Success

&#9989;	Row 73: Success

&#9989;	Row 74: Success

&#9989;	Row 75: Success

&#9989;	Row 76: Success

&#9989;	Row 77: Success

&#9989;	Row 78: Success

&#9989;	Row 79: Success

&#9989;	Row 80: Success

&#9989;	Row 81: Success

&#9989;	Row 82: Success

&#9989;	Row 83: Success

#### Results: PASS
---
### Comparing samples in both files . . .

&#10060;	 Sample "LN-229" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "SNU-1040" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "UACC-893" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "ESO51" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "BL-41" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "SW962" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "ES1" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "NCI-H1395" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 Sample "H2803" is in "metadata.tsv.gz" but not in "data.tsv.gz"

&#10060;	 More errors are not being printed...

<font color="red">Total sample mismatch errors: 976</font>

#### Results: **<font color="red">FAIL</font>**

---
### Testing Directory after cleanup . . .

#### Results: PASS
---
