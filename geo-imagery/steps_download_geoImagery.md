# Tropical cyclone related satellite imagery

1. Identify storms of interest by basin/year.
   - The [tropycal](https://tropycal.github.io/tropycal/data.html) package is **not** comprehensive enough- it does **not** include all kinds of storms we may be interested (from an imagery point of view); it does not include [Medicanes](https://en.wikipedia.org/wiki/Mediterranean_tropical-like_cyclone).
   - Therefore, we'll use [wikipedia](https://www.wikipedia.org/). Search "2023 atlantic hurricane season"; `basin` = atlantic, `year` = 2023.

2. Gather chronological list of all storms.
   - For [Atlantic, 2023 see this page.](https://en.wikipedia.org/wiki/2023_Atlantic_hurricane_season#Seasonal_summary)
   - Imagery for category >= 4 is easiest to interprest. Why?
     - The structure of the clouds (hurricane _eye_ and spiral _bands_), so we'll start withh them.
     - They are the most _destructive_ ones as well.
   - For e.g. we'll consider, [Franklin (C4)](https://en.wikipedia.org/wiki/Hurricane_Franklin_(2023)). 
   - **Note**: The [Timeline](https://en.wikipedia.org/wiki/Timeline_of_the_2023_Atlantic_hurricane_season) has hyperlinks for each storm to ease our life!

3. Identify storm timelines. 
   - [Franklin (2023)](https://en.wikipedia.org/wiki/Hurricane_Franklin_(2023)) formed (dissipated) on 08/20 (09/10), 2023. Typically in the beginning of the storm, until it attains category >= 1, the clouds bands/structure is _unorganized_, so we'll skip that part of the storm's life cycle. 
   - ["...Franklin entered a more favorable environment for development on August 25 and promptly intensified into a Category 1 hurricane the next morning."](https://en.wikipedia.org/wiki/Hurricane_Franklin_(2023)#Meteorological_history)
   - ["That same day, Franklin began losing its tropical characteristics, and by 21:00 UTC on September 1 it had become a hurricane-force extratropical cyclone."](https://en.wikipedia.org/wiki/Hurricane_Franklin_(2023)#Meteorological_history)

4. Find satellite images for a time-range.
   - For Franklin (2023): 08/25- 09/01, 2023.
   - Google: "geostationary satellite image archive". Even though our focus is on storms, we have our hands on entire geostationary database.
     - Go to the [NOAA Office of Satellite and Product Operations] (https://www.ospo.noaa.gov/Products/imagery/archive.html). NOAA operates _weather and operational forecasting_ satellites, NASA satellites are for _science missions_.
     - [Satellite Inventory Browser](https://www.ssec.wisc.edu/datacenter/goes-archive/)
     - For 08/25- 09/01, 2023, Atlantic, use [**GOES-16 imagery**](https://inventory.ssec.wisc.edu/inventory/?date=2011/10/18&time=&satellite=GOES-16&search=1#search&start_time:2017-12-19%2000:00;end_time:2017-12-19%2023:59;satellite:GOES-16;). It's imager has [**16-bands**](https://en.wikipedia.org/wiki/GOES-16) in the infrared part of the electromagnetic spectrum, we'll use the [11.2 micro meter band](https://en.wikipedia.org/wiki/GOES-16#Advanced_Baseline_Imager_(ABI)) which provides imagery of [clouds and water vapor](https://www.star.nesdis.noaa.gov/goes/documents/ABIQuickGuide_Band14.pdf).
   - Follow [these instructions steps](https://drive.google.com/drive/folders/16tp_ehG0ZOmSwY55yo4L1q701i-xL7uQ?usp=drive_link)
   
     A. [Search](https://inventory.ssec.wisc.edu/inventory/)
     
     B. [Query](https://inventory.ssec.wisc.edu/inventory/?date=2011/10/18&time=&satellite=GOES-16&search=1#search)
     
     C. Fill in search parameters: `Date`, `Satellite`, `Type`, `Coverage` (= Conus, which zooms in to our region of interest); and `search`.
     
     D. Once all criteria are filled in, it will take you to [this page for 08/25/2023](https://inventory.ssec.wisc.edu/inventory/?date=2011/10/18&time=&satellite=GOES-16&search=1#search&start_time:2023-08-25%2000:00;end_time:2023-08-25%2023:59;satellite:GOES-16;coverage:CONUS;), try "scripts for downloading data". Register to get an [API key.](https://mcfetch.ssec.wisc.edu/#register)
   
   - GOES ABI takes an image every 5-min, for our study, we'll extract hourly.
 
  
 **Note**:
 
   	  - Read [this ESA page reg different satellite orbits.](https://www.esa.int/Enabling_Support/Space_Transportation/Types_of_orbits)
     - If you want **only one** image, [try hurricane imagery archive.](https://www.nesdis.noaa.gov/imagery/hurricanes/hurricane-imagery-archive)
