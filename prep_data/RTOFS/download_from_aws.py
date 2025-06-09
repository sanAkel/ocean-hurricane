#!/usr/bin/env python3

#on wcoss-2
# module use /apps/dev/modulefiles/
# ml ve/evs/2.0_py312

import sys
import os
import glob as glob
import numpy as np
import pandas as pd
import xarray as xr

# inputs
system, version = ["rtofs", "v2.4"]

#start_date, end_date = ["20240619", "20240719"]
#start_date, end_date = ["20240914", "20241017"]
start_date, end_date = ["20241028", "20241119"]
hSkip=6 # skip hour
hours = np.arange(0, 25, hSkip)
# --

if system == "rtofs":
  bucket = "noaa-nws-rtofs-pds"
  oPath = "/lfs/h2/emc/ptmp/santha.akella/data/rtofs/test/out/"
elif system == "hafs":
  bucket = "noaa-nws-hafs-pds"
else:
  print('UNKNOWN/not yet coded bucket! Fix and try again.')
url_base = f"https://{bucket}.s3.amazonaws.com/{system}."
# --

data_dates = pd.date_range(start=start_date, end=end_date)

# Download
# --
url = ""
for dd in data_dates:
  dSTR = dd.strftime("%Y%m%d")
  print(f"Downloading data for:\t {dSTR}")
  url = url_base + dd.strftime("%Y%m%d") + "/" + system+"_glo.t00z."

  for hr in hours:
    output_dir = oPath + dSTR + "/" + str(hr).zfill(2)
    os.system(f"mkdir -p {output_dir}")
    if hr == 0:
      a_file, b_file = ["n00.archs.a.tgz", "n00.archs.b"]
    else:
      a_file, b_file = ["n-"+str(hr).zfill(2) + ".archs.a.tgz",\
                        "n-"+str(hr).zfill(2) + ".archs.b"]
    a_file_url = url + a_file
    b_file_url = url + b_file

    a_file_tar = dd.strftime("%Y%m%d") + "_" + a_file
    a_file = system+"_glo.t00z." + a_file
    b_file = system+"_glo.t00z." + b_file

    #print(a_file_url, b_file_url)
    # download
    CMD1 = f"wget -q {a_file_url} -O {a_file_tar}"
    CMD2 = f"wget -q {b_file_url} -O {b_file}"
    os.system(CMD1)
    os.system(CMD2)
    #print(CMD1)

    CMD3 = f"mv {a_file_tar} {output_dir}"
    CMD4 = f"mv {b_file} {output_dir}"
    os.system(CMD3)
    os.system(CMD4)

print("\n\n")

# Extract (untar) .tgz ("a", i.e., archive file)
# --
for dd in data_dates:
  dSTR = dd.strftime("%Y%m%d")
  print(f"Extracting data for:\t {dSTR}")
  for hr in hours:
    output_dir = oPath + dSTR + "/" + str(hr).zfill(2) + "/"
    #print(f"{output_dir}")

    tgz_fName = glob.glob(output_dir + "*.tgz")
    #print(f"{tgz_fName[0]}")

    CMD_e1 = f"tar xvzf {tgz_fName[0]} -C {output_dir}"
    CMD_e2 = f"rm -f {tgz_fName[0]}"

    os.system(CMD_e1)
    os.system(CMD_e2)
