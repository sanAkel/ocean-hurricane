# Notebooks were used to gather data and create plots that were presented:
  - [Abstract](https://cdn-assets.inwink.com/e2ed7ccb-dbb5-4dc9-9b30-9a6876d1fc19/89c38400-c147-46f6-a577-4c3d876be1e3)
  - [Slides](https://storageprdv2inwink.blob.core.windows.net/e2ed7ccb-dbb5-4dc9-9b30-9a6876d1fc19/77439c32-c4d0-4d5c-8e58-496dfeb78683)

# Description of scripts:

- Get storm trajectory and variables: `get_track.ipynb`
- Download data from AVISO: L4 ADT, geostrophic currents, SLA: `aviso_cmems.ipynb`
- Same as above, but from Glorys12: `mercator_glorys12_cmems.ipynb`
- Plot and compare AVISO and Glorys12 fields before days/before/on min MSLP day: `plot_aviso_glorys12_before_after_TC.py`
- Glue png files to make a single gif animated file: `png_to_gif.py`
- Download Glorys12 subsurface data at time and location of storm- along storm track: `download_along_track.ipynb`
  - **Note**: It takes a while (about 60 min) for this API to extract such data.
- Download and animate (gif) satellite data products for any storm: `animate_satellite_data_hurr_track.ipynb`. 
  Satellite products:
  - AVISO (SLA, Geostrophic currents, SSH); daily.
  - OSTIA SST; daily.
  - CNS SSS, density; daily (near-real time version).
- Compare satellite data products with ocean reanalysis (Mercator Glorys for now), comparison is done over a few days before, during, and after the hurricane:
  - AVISO ADT with Glorys SSH `compare_SSH_GLO12_one_HURR.ipynb`
  - OSTIA SST with Glorys thetao (top level): `compare_SST_GLO12_one_HURR.ipynb`
  - CNS SSS with Glorys so (top level): `compare_SSS_GLO12_one_HURR.ipynb`
  - GLOBCURRENT surface (z=0) speed with that from Glorys: `compare_surfCurrents_GLO12_one_HURR.ipynb`
- Plot storm track (mslp, wind speed); SSH, SST, SSS; Subsurface T and S: `plot_before_after_storm.ipynb`

- `prep_data/`: Contains scripts to download different datasets and prepare them for inter-comparison.

### Remarks: 
- Following are being kept, but not needed because above plotting scripts deprecate them, but kept for future use:
  - Plot AVISO fields on min MSLP day: `plot_aviso_fields_at_min_SLP.ipynb`
  - Same as above, but for many days: `plot_aviso_fields_hurr_track.ipynb`
  - A few lines of code will repeat in many notebooks to read downloaded storm data (using tropycal), this was done to avoid package conflicts on [google colab](https://colab.research.google.com/). 
    - All these notebooks are meant to run in colab environment for enhance portability.
