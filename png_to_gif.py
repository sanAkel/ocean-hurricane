#!/usr/bin/env python

from PIL import Image
import glob as glob
import pandas as pd

# create an empty list called images
def make_gif_from_pngs(data_path, png_files, fPref, fSuff='.gif', DUR=1000, LOOP=0):
  images = []
  for filename in png_files:
    im = Image.open(filename)
    images.append(im)

  # save as a gif
  fOut = data_path+fPref + fSuff
  images[0].save(fOut,save_all=True,
               append_images=images[0:],
               optimize=False,
               duration=DUR, # Duration in milliseconds
               loop=LOOP) # infinite loop
  print('\nSaved:\t{}\n'.format(fOut))
# --

year=2024
myBasin='north_atlantic'
cat_threshold=4
fTypes = ['adt', 'U']

data_path = '/work/noaa/marine/sakella/' + '/data/hurr/{}/'.format(year)
png_files_path = '/work/noaa/marine/sakella/' + 'ssh_tc/figs/'

# Read hurricane season summary
track_summ_fName = data_path + 'hurdat2_{}_{}.csv'.format(myBasin, year)
print("Reading {} summary data from:\n{}\n".format(year, track_summ_fName))

season_data=pd.read_csv(track_summ_fName)
major_hurr_names = season_data['name'][season_data['category'] >=cat_threshold]

print("Chosen storms:")
for hurr_name in major_hurr_names:
  print(hurr_name)
  for fType in fTypes:
   fNames = sorted( glob.glob( png_files_path + hurr_name+'*{}*'.format(fType)+'.png'))
   fPref_with_path = fNames[0].split('{}'.format(year))[0]
   fPref = fPref_with_path.split('/')[-1]
   #print(fPref)
   make_gif_from_pngs(png_files_path+'gif/', fNames, fPref)
