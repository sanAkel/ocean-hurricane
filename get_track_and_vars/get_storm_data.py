#!/usr/bin/env python3

import numpy as np
import xarray as xr

import cartopy.crs as ccrs
import cartopy.feature as cfeature

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# To avoid warning messages
import warnings
warnings.filterwarnings('ignore')

# https://tropycal.github.io/tropycal/examples/tracks.storm.html
from tropycal import tracks, rain
# -----------------------------------------------

# INPUTS - should be argparse'ed
plot_seas = False
basin = 'north_atlantic'
year = 2021
tc_name = 'sam'
# -----------------------------------------------

# Initialize
# https://tropycal.github.io/tropycal/api/generated/tropycal.tracks.TrackDataset.html#tropycal.tracks.TrackDataset

basin = tracks.TrackDataset(basin=basin, source='hurdat', include_btk=False) # include most recent season

# print summary of chosen year/season
season = basin.get_season(year)
print(season)

# plot season
if plot_seas == True:
  season.plot(map_prop={'figsize':(12,8),'linewidth':0.5, 'state_alpha':0.5})
  fName_fig = str(year) + '_' + 'north_atlantic' + '.png'
  plt.savefig(fName_fig, dpi=120)
  plt.close('all')

# save summary
seas_summary = season.summary()

# check if chosen storm name matches those in database
# and save storm data- if it became a hurricane
storm_exists = True
hurr_cat = True
fName_save = tc_name + '_' + str(year) + '.nc'
 
if not tc_name.upper() in seas_summary['name']:
  print('\nInput storm name was not found in database.\nCheck if the storm by that name exists and try again.\n')
  storm_exists = False

if storm_exists:
  myStorm = basin.get_storm((tc_name, year))

  # Did it attain hurricane status?
  if len(myStorm.mslp[myStorm.type=='HU']) <= 0:
    print('\n{} was never categorized as a hurricane.'.format(tc_name))
    hurr_cat = False

if storm_exists and hurr_cat:
  storm_data = myStorm.to_xarray()
  storm_data.to_netcdf(fName_save)
  print('\nData was saved to:\t{}'.format(fName_save))
  print('\nAll Done.')
# -----------------------------------------------

