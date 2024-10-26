#!/usr/bin/env python
#
# converted from notebook version
# jupyter nbconvert --to=python plot_aviso_glorys12_after_TC.ipynb
#

import warnings
warnings.filterwarnings('ignore')

import xarray as xr
import numpy as np
import pandas as pd
import cartopy.crs as ccrs

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


def get_plot_times(track_ds, day_buffer):
    # Date of minimum MSLP/highest intensity, if it was sustained (in time), pick first occurence
    tMinSLP=track_ds.mslp.where(track_ds.mslp==track_ds.mslp.min(), drop=True).time.values[0]
    print("Minimum SLP on:\t{}".format(tMinSLP))

    tPlot = [track_ds.time[0].values- np.timedelta64(day_buffer, 'D'), track_ds.time[0].values,\
             tMinSLP,\
             track_ds.time[-1].values, track_ds.time[-1].values + np.timedelta64(day_buffer, 'D')]
    return tPlot

def plot_aviso_glorys12_time_instant(aviso_ds, glorys12_ds, track_ds, vName_aviso, vName_glorys12, time_inst, DPI=120):
    if vName_aviso == "surfCurr":
        vMin, vMax, cMap = [0., 1., "Blues"]
        #label_str = "Geostrophic current speed [ms$^{-1}$]"
        label_str = "Current speed [ms$^{-1}$]"
        track_color = 'r'
    else: #vName_aviso == "adt":
        vMin, vMax, cMap = [-1., 1., "gist_ncar"]
        label_str = "ADT [m]"
        track_color = 'k'

    # Plot bounding box
    lat_start, lat_end=[track_ds.lat.min().values-dLat, track_ds.lat.max().values+dLat]
    lon_start, lon_end=[track_ds.lon.min().values-dLon, track_ds.lon.max().values+dLon]

    tStr = "{}".format(time_inst.astype(str).split('T')[0])+ '-'+\
           "{}".format(time_inst.astype(str).split('T')[1].split(':')[0])+'UTC'

    fig=plt.figure(figsize=(16, 4))

    ax1=plt.subplot(121, projection=ccrs.PlateCarree())
    ax1.coastlines()
    #ax1.add_feature(cfeature.LAND, zorder=100, edgecolor='k')
    aviso_ds[vName_aviso].sel(latitude=slice(lat_start, lat_end),\
                        longitude=slice(lon_start, lon_end)).sel(time=time_inst, method="nearest").\
    plot(ax=ax1, vmin=vMin, vmax=vMax, cmap=cMap, add_colorbar=False, transform=ccrs.PlateCarree())#,\
    #cbar_kwargs={'pad':0.01, 'label':label_str})
    ax1.scatter(track_ds.lon, track_ds.lat, s=track_ds.vmax/5., c=track_color, marker='o',\
                edgecolor=None, transform=ccrs.PlateCarree())
    ax1.text(lon_start, lat_end+1, "(a)", fontsize=14, transform=ccrs.PlateCarree())
    ax1.text(track_ds.lon[0].values, track_ds.lat[0].values, "{}".format(track_ds.time[0].values.astype(str).split('T')[0], fontsize=1),\
            transform=ccrs.PlateCarree())
    ax1.text(track_ds.lon[-1].values, track_ds.lat[-1].values, "{}".format(track_ds.time[-1].values.astype(str).split('T')[0], fontsize=1),\
            transform=ccrs.PlateCarree())
    ax1.set_xlim([lon_start, lon_end]), ax1.set_ylim([lat_start, lat_end])
    ax1.set_title('AVISO {}'.format(tStr))
    #
    ax2=plt.subplot(122, projection=ccrs.PlateCarree())
    ax2.coastlines()
    #ax2.add_feature(cfeature.LAND, zorder=100, edgecolor='k')
    glorys12_ds[vName_glorys12].sel(latitude=slice(lat_start, lat_end),\
                           longitude=slice(lon_start, lon_end)).sel(time=time_inst, method="nearest").\
    plot(ax=ax2, vmin=vMin, vmax=vMax, cmap=cMap, add_colorbar=True, transform=ccrs.PlateCarree(),\
    cbar_kwargs={'pad':0.01, 'label':label_str})
    ax2.scatter(track_ds.lon, track_ds.lat, s=track_ds.vmax/5., c=track_color, marker='o',\
                 edgecolor=None, transform=ccrs.PlateCarree())
    ax2.text(lon_start, lat_end+1, "(b)", fontsize=14, transform=ccrs.PlateCarree())
    #ax2.text(track_ds.lon[0].values, track_ds.lat[0].values, "{}".format(track_ds.time[0].values.astype(str).split('T')[0], fontsize=1),\
    #        transform=ccrs.PlateCarree())
    #ax2.text(track_ds.lon[-1].values, track_ds.lat[-1].values, "{}".format(track_ds.time[-1].values.astype(str).split('T')[0], fontsize=1),\
    #        transform=ccrs.PlateCarree())
    ax2.set_xlim([lon_start, lon_end]), ax1.set_ylim([lat_start, lat_end])
    ax2.set_title('GLORYS12 {}'.format(tStr))
    #
    plt.subplots_adjust(wspace=-0.1)
    figName = 'figs/'+hurr_name + '_aviso_glorys12_' + vName_aviso +'_{}'.format(tStr)+'.png'
    plt.savefig(figName, dpi=DPI)
    plt.close('all')

## Inputs

year=2023
myBasin='north_atlantic'
cat_threshold = 4

day_buffer = 2 # extract CMEMS data hurricane start day-day_buffer --> end day+day_buffer
dLat, dLon = [10, 10] # plot bounding box beyond storm extent

## Read track data, plot AVISO and GLORYS12 fields

data_path = '/work/noaa/marine/sakella/' + '/data/hurr/{}/'.format(year)

track_summ_fName = data_path + 'hurdat2_{}_{}.csv'.format(myBasin, year)
print("Reading {} summary data from:\n{}\n".format(year, track_summ_fName))

season_data=pd.read_csv(track_summ_fName)
major_hurr_names = season_data['name'][season_data['category'] >=cat_threshold]

print("Storms chosen by category:")
for hurr_name in major_hurr_names:
  print(hurr_name)

  track_fName = "{}/{}_{}_{}.nc".format(data_path, str(year), myBasin, hurr_name)
  aviso_fName = "{}/{}_{}_{}_AVISO_L4.nc".format(data_path, str(year), myBasin, hurr_name)
  glorys12_fName = "{}/glorys12/".format(data_path) 
  print("{}\n{}\n{}".format(track_fName, aviso_fName, glorys12_fName))
  track_ds = xr.open_dataset(track_fName)
  aviso_ds = xr.open_dataset(aviso_fName)
  glorys12_ds = xr.open_mfdataset(glorys12_fName+"/*.nc")

  aviso_U = np.sqrt(aviso_ds.ugos**2+aviso_ds.vgos**2)
  glorys12_U = np.sqrt(glorys12_ds.uo**2+glorys12_ds.vo**2)
  
  aviso_ds['surfCurr'] = aviso_U
  glorys12_ds['surfCurr'] = glorys12_U
    
  tPlot = get_plot_times(track_ds, day_buffer) # Pick a few time slices (to plot)
  for time_inst in tPlot:
      print("Plotting at:\t{}".format(time_inst))
      
      plot_aviso_glorys12_time_instant(aviso_ds, glorys12_ds, track_ds, "surfCurr", "surfCurr", time_inst)
      plot_aviso_glorys12_time_instant(aviso_ds, glorys12_ds, track_ds, "adt", "zos", time_inst)
