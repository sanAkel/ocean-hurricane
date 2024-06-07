#!/usr/bin/env python3

import argparse
import os
import urllib3
import shutil
import pandas as pd

def download_file(url, output_fName):
  # https://stackoverflow.com/questions/17285464/whats-the-best-way-to-download-file-using-urllib3
  http = urllib3.PoolManager()
  with open(output_fName, 'wb') as out:
    r = http.request('GET', url, preload_content=False)
    shutil.copyfileobj(r, out)

  print("\n\nDownloaded: {}".format(output_fName))

  if not os.path.isfile(output_fName):
    print("\n\nError in downloading file:{}".format(output_fName))
    print("Check URL:\n{}\n\n".format(url))
# --

# fixed parameters
myKEY = "yug2253g-jeua-rbjy-l0x1-ntrk21rqve56"
LAT_LON = "25.0+75.2"
SIZE = "216+512"
SAT = "GOES16"
COV = "FD" #"CONUS"
BAND = str(14)
base_url = "https://mcfetch.ssec.wisc.edu/cgi-bin/mcfetch?dkey="
# --

# user inputs
get_inputs = argparse.ArgumentParser(prog='\nget_geo_images.py',\
description='Download Geostationary satellite imagery between start - end dates.', usage='%(prog)s [options]')

get_inputs.add_argument('--start_date', type=str,\
                        metavar='starting date', default="20230825")

get_inputs.add_argument('--end_date', type=str,\
                        metavar='ending date', default="20230901")
args = get_inputs.parse_args()
# --

date_s, date_e = [args.start_date, args.end_date]
for dd in pd.date_range(date_s, date_e):
  #print( dd.strftime('%Y%m%d'))

  for hr in range(0, 24):
    UTC_hr = str(hr).zfill(2)

    url = base_url+myKEY+\
          "&satellite=" + SAT+\
          "&output=PNG"+\
          "&size=" + SIZE+\
          "&lat=" + LAT_LON+\
          "&MAP=YES&GEORES=YES&gray=YES" +\
          "&date=" + dd.strftime('%Y%m%d')+\
          "&time=" + UTC_hr + ':01:17'\
          "&coverage=" + COV+\
          "&band=" + BAND

    #print(url)
    output_fName = SAT + "_b_"+BAND + "_" + dd.strftime('%Y%m%d') + "_" + UTC_hr + "z.png"
    output_path = "/Users/sakella/Desktop/mm/pp/qq/figs/"
    #print(output_path+output_fName)
    download_file(url, output_path+output_fName)
