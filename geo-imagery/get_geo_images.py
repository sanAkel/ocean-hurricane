#!/usr/bin/env python3

import argparse
import os
import urllib3
import shutil
import pandas as pd

def download_file(url, output_fName):
    http = urllib3.PoolManager()
    with http.request('GET', url, preload_content=False) as response, open(output_fName, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    
    print(f"\n\nDownloaded: {output_fName}")
    
    if not os.path.isfile(output_fName):
        print(f"\n\nError in downloading file: {output_fName}")
        print(f"Check URL:\n{url}\n\n")

def construct_url(date, hour, key, sat, size, lat_lon, cov, band):
    base_url = "https://mcfetch.ssec.wisc.edu/cgi-bin/mcfetch?dkey="
    url = (f"{base_url}{key}&satellite={sat}&output=PNG&size={size}&lat={lat_lon}"
           f"&MAP=YES&GEORES=YES&gray=YES&date={date}&time={hour}:01:17&coverage={cov}&band={band}")
    return url

def main():
    parser = argparse.ArgumentParser(
        prog='get_geo_images.py',
        description='Download Geostationary satellite imagery between start - end dates.',
        usage='%(prog)s [options]'
    )
    
    parser.add_argument('--start_date', type=str, metavar='starting date', default="20210827")
    parser.add_argument('--end_date', type=str, metavar='ending date', default="20210828")
    args = parser.parse_args()
    
    key = "o569q7mv-oftx-sdoz-kbat-9ll6heyu8r8j"
    lat_lon = "25.0+75.2"
    size = "216+512"
    sat = "GOES16"
    cov = "FD"
    band = "14"
    
    start_date, end_date = args.start_date, args.end_date
    output_dir = "/Users/emonc/Documents/internship2024/figs_ida/"
    
    for date in pd.date_range(start_date, end_date):
        date_str = date.strftime('%Y%m%d')
        for hour in range(24):
            utc_hour = str(hour).zfill(2)
            url = construct_url(date_str, utc_hour, key, sat, size, lat_lon, cov, band)
            output_fName = f"{sat}_b_{band}_{date_str}_{utc_hour}z.png"
            download_file(url, os.path.join(output_dir, output_fName))

if __name__ == "__main__":
    main()
