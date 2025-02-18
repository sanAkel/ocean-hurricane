# Description of scripts:

- [Get storm trajectory and variables](https://github.com/sanAkel/ocean-hurricane/blob/main/get_track.ipynb)
- [Download data from AVISO: L4 ADT, geostrophic currents, SLA](https://github.com/sanAkel/ocean-hurricane/blob/main/aviso_cmems.ipynb)
- [Same as above, but from Glorys12](https://github.com/sanAkel/ocean-hurricane/blob/main/mercator_glorys12_cmems.ipynb)
- [Plot and compare AVISO and Glorys12 fields before days/before/on min MSLP day](https://github.com/sanAkel/ocean-hurricane/blob/main/plot_aviso_glorys12_before_after_TC.py)
- [Glue png files to make a single gif animated file](https://github.com/sanAkel/ocean-hurricane/blob/main/png_to_gif.py)
- [Download Glorys12 subsurface data at time and location of storm- along storm track](https://github.com/sanAkel/ocean-hurricane/blob/main/download_along_track.ipynb)
  - **Note**: It takes a while (about 60 min) for this API to extract such data.
- [Download and animate (gif) satellite data products for any storm](https://github.com/sanAkel/ocean-hurricane/blob/main/animate_satellite_data_hurr_track.ipynb). Satellite products:
  - AVISO (SLA, Geostrophic currents, SSH); daily.
  - OSTIA SST; daily.
  - CNS SSS, density; daily (near-real time version).
- Compare satellite data products with ocean reanalysis (Mercator Glorys for now), comparison is done over a few days before, during, and after the hurricane:
  - [AVISO ADT with Glorys SSH.](https://github.com/sanAkel/ocean-hurricane/blob/main/compare_SSH_GLO12_one_HURR.ipynb)
  - [OSTIA SST with Glorys thetao (top level).](https://github.com/sanAkel/ocean-hurricane/blob/main/compare_SST_GLO12_one_HURR.ipynb)
  - [CNS SSS with Glorys so (top level)](https://github.com/sanAkel/ocean-hurricane/blob/main/compare_SSS_GLO12_one_HURR.ipynb)
  - [GLOBCURRENT surface (z=0) speed with that from Glorys](https://github.com/sanAkel/ocean-hurricane/blob/main/compare_surfCurrents_GLO12_one_HURR.ipynb)
- [Plot storm track (mslp, wind speed); SSH, SST, SSS; Subsurface T and S](https://github.com/sanAkel/ocean-hurricane/blob/main/plot_before_after_storm.ipynb)

- `prep_data/`: Contains scripts to download different datasets and prepare them for inter-comparison.

### Remarks: 
- Following are being kept, but not needed because above plotting scripts deprecate them, but kept for future use:
  - [Plot AVISO fields on min MSLP day](https://github.com/sanAkel/ocean-hurricane/blob/main/plot_aviso_fields_at_min_SLP.ipynb)
  - [Same as above, but for many days](https://github.com/sanAkel/ocean-hurricane/blob/main/plot_aviso_fields_hurr_track.ipynb)
- A few lines of code will repeat in many notebooks to read downloaded storm data (using tropycal), this was done to avoid package conflicts     on [google colab](https://colab.research.google.com/). All these notebooks are meant to run in colab environment for enhance portability.
- If it was allowed to mount google drive (on certain platforms), much of our life will be simpler. But when did _all_ folks really understand developers needs?
