#IMPORT STATEMENTS 
import netCDF4
import numpy as np
import pandas as pd
import requests
import urllib
import os
import logging
from pathlib import Path
import xarray as xr


#function to read the file 
def read_nc_file(year):
    try:
        #reads the file 
        file_name = f'hgt.{year}.nc'
        cwd = os.getcwd()
        #gets file path
        file_path = f'{cwd}/src/data/{file_name}'
        #uses xarray to open the file 
        ds = xr.open_dataset(file_path)
        #turns the read in file to a dataframe 
        df = ds.to_dataframe()
        print(df.head())
        f = netCDF4.Dataset(file_path)
        logging.info('Successfully read data from {year}.')
        return f
    except:
        logging.error('Unexpected error while reading data from {year}.')

nc = read_nc_file(1948)
hgt = nc.variables['hgt']
print('\n\n')
print(hgt)
