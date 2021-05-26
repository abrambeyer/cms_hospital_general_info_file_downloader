
Python Scripts:

cms_star_rating_hospital_general_information_downloader.py: on
Opens a Chrome browser,
collects the most recent revised flatfile from each archive year available on the page,
opens the 'Hospital General Information.csv' csv file into a pandas dataframe,
and unions all years together while creating a 'Year' column to indicate which year
the data came from.

helpers.py:  Stores all functions necessary for the script.


Output Description:

Final unioned excel file is output to the data folder by default.

Output is an excel file because Hospital facility IDs (Medicare IDs) can have
a leading zero.  A csv file may accidently truncate the leading zero, therefore,
I am writing the final dataframe to an excel file.


What the cms_star_rating_hospital_general_information_downloader.py script does:

Core python script which runs all functions necessary to download and union the 
most recent cms hospital general information file for each available year on CMS' archive site.