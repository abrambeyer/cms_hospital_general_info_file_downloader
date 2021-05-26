# cms_hospital_general_info_file_downloader

The project collects and wrangles all archived Hospital General Information.csv files from cms.gov  (Centers for Medicare and Medicaid Services)  *[archive page](https://data.cms.gov/provider-data/archived-data/hospitals)*.  The purpose of this project is collect all yearly revised files, join them together.  Finally, perform and exploratory analysis of all CMS hospital Overall CMS Star Ratings.

The data is made available by *[CMS.gov](https://www.cms.gov/Medicare/Quality-Initiatives-Patient-Assessment-Instruments/HospitalQualityInits/HospitalCompare)*

The goal of this project is to better understand the CMS Star Overall Rating for all Medicare hospitals.

Hospital Compare provides data on over 4,000 Medicare-certified hospitals, including acute care hospitals, critical access hospitals (CAHs), children’s hospitals, Veterans Health Administration (VHA) Medical Centers, and hospital outpatient departments.


# Python Project Folder: cms_star_rating_hospital_general_info_gather

## What this project does:
    
1. Opens CMS archive data site
2. Collects all revised flatfile zipped folders
3. Selects the most recent zipped folder for each year on the page
4. Reads the Hospital General Information.csv file within each year's zipped folder into pandas dataframe.
5. Creates new year column for each file
6. Renames some columns so all files are aligned
7. Unions all file dataframes together
8. Writes final dataframe to an excel file in the data folder.

* Includes 2 main python scripts:
  * cms_star_rating_hospital_general_information_downloader.py  (runs the main function)
  * helpers.py   (holds all necessary functions and imports necessary packages)

* Final Output:
  Should output an Excel file to the data folder which includes all revised flatfile "Hospital General Informationc.csv" file data for every year on 
  the *[archive page](https://data.cms.gov/provider-data/archived-data/hospitals)* excluding data for years 2015 and 2014.  2015 and 2014 are excluded because their
  Hospital General Information files only include hospital contact information rather than CMS Star Rating.


* Attribution:

  All Hospital Compare websites are publically accessible. As works of the U.S. government, Hospital Compare data are in the public domain and permission is not required to  reuse them. An attribution to the agency as the source is appreciated. Your materials, however, should not give the false impression of government endorsement of your commercial products or services.
