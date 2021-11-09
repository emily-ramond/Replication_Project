# IMPORT STATEMENTS
import netCDF4
import numpy as np
import requests
import urllib
import os
import logging
from pathlib import Path

# FUNCTION TO DOWNLOAD DATA 
def download_file(year):
    try:
        file_name = f'hgt.{year}.nc' # grabs file names in hgt.year format
        cwd = os.getcwd()
        file_path = f'{cwd}/src/data/{file_name}'
        
        if Path(file_path).exists():
            logging.info(f'Data for {year} is already downloaded.') #sends logging info to log file
        else:
            url = 'https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/' #location of file  
            file_url = f'{url}{file_name}' 
            file = requests.get(file_url) #requests the file 
            
            
            open(f'src/data/{file_name}','wb').write(file.content) #writes the file content 
            logging.info(f'Dara for {year} successfully downloaded.') #reports successful file download 

    except:
        logging.error('Unexpected error while downloading data from {year}.') #log any errors 

#downloads the files for each year ***NEED TO ADD VARIABLES FOR EASY USE IN FUTURE***
for i in range(11):
    yr = 2011 + i
    download_file(yr)

