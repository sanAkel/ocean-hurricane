# Description of scripts:

- [Get storm trajectory and variables](https://github.com/sanAkel/ocean-hurricane/blob/main/get_track.ipynb)
- [Download data from AVISO: L4 ADT, geostrophic currents, SLA](https://github.com/sanAkel/ocean-hurricane/blob/main/aviso_cmems.ipynb)
- [Same as above, but from Glorys12](https://github.com/sanAkel/ocean-hurricane/blob/main/mercator_glorys12_cmems.ipynb)
- [Plot and compare AVISO and Glorys12 fields before days/before/on min MSLP day](https://github.com/sanAkel/ocean-hurricane/blob/main/plot_aviso_glorys12_before_after_TC.py)
- [Glue png files to make a single gif animated file](https://github.com/sanAkel/ocean-hurricane/blob/main/png_to_gif.py)
- [Download Glorys12 subsurface data at time and location of storm- along storm track](https://github.com/sanAkel/ocean-hurricane/blob/main/download_along_track.ipynb)
  - **Note**: It takes a while (about 60 min) for this API to extract such data.

### Remarks: 
- Following are being kept, but not needed because above plotting scripts deprecate them, but kept for future use:
  - [Plot AVISO fields on min MSLP day](https://github.com/sanAkel/ocean-hurricane/blob/main/plot_aviso_fields_at_min_SLP.ipynb)
  - [Same as above, but for many days](https://github.com/sanAkel/ocean-hurricane/blob/main/plot_aviso_fields_hurr_track.ipynb)
  - A few lines of code will repeat in many notebooks to read downloaded storm data (using tropycal), this was done to avoid package conflicts     on [google colab](https://colab.research.google.com/). All these notebooks are meant to run in colab environment for enhance portability.
  - If NOAA security would allow mounting google drive, much of our life will be simpler. But when did _security_ folks really understand developers needs?
