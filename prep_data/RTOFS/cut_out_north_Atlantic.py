#!/usr/bin/env python3

#on wcoss-2
#module use /apps/dev/modulefiles/
#ml ve/evs/2.0_py312

import glob as glob
import xarray as xr

input_data_path = "/lfs/h2/emc/ptmp/santha.akella/data/arch2nc/v2p5_bad/"
output_data_path = "/lfs/h2/emc/ptmp/santha.akella/data/arch2nc/v2p5_bad/nATL_cut_out/"

# manually figure out box dimensions
ys, ye = [1300, 2200]
xs, xe = [2200, 3500]  
# --

inFiles = sorted( glob.glob(input_data_path+"*.nc"))
for fName in inFiles:
  inFile = fName.split('/')[-1]
  print(f'Reading... {inFile}')
  
  in_ds = xr.open_dataset(fName)
  out_ds = in_ds.sel(X=slice(xs, xe), Y=slice(ys, ye))

  output_fName = output_data_path + "nATL_"+ inFile
  out_ds.to_netcdf(output_fName)
  print(f'Saved... {output_fName}')
