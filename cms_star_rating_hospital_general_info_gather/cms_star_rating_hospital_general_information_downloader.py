# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:19:22 2021

@author: nm184423
"""
################################################################################################
## AUTHOR:  R. Abram Beyer
## DESCRIPTION:  Core python script which runs all functions necessary to 
##                download and union the most recent cms hospital general information
##               file for each available year on CMS' archive site.


##What this project does:
    
##opens CMS archive data site
##collects all revised flatfile zipped folders
##selects the most recent zipped folder for each year on the page
##reads the Hospital General Information.csv file within each year's zipped folder into pandas dataframe.
##creates new year column for each file
##renames some columns so all files are aligned
##unions all file dataframes together
##writes final dataframe to an excel file in the data folder.



################################################################################################
## UPDATE LOG:


################################################################################################



import helpers


helpers.main_cms_revised_flatfile_downloader()
