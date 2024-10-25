## Full file
```
 copernicusmarine get --dataset-id cmems_mod_glo_phy_anfc_0.083deg_PT1H-m --credentials-file ~santa/ -nd --output-directory /home/santa/marine/data/hurr/2024/glorys12 --filter "*202406*"
```

## Subset

- 1 time slice (00 UTC):
```
copernicusmarine subset --dataset-id cmems_mod_glo_phy_anfc_0.083deg_PT1H-m --credentials-file ~santa/ -o ./glorys12 -t 2024-06-01 -T 2024-06-01 --minimum-latitude 0 --maximum-latitude 65 --minimum-longitude -110 --maximum-longitude 0
```

- 1 day (24 hours):
```
copernicusmarine subset --dataset-id cmems_mod_glo_phy_anfc_0.083deg_PT1H-m --credentials-file ~santa/ -o ./glorys12 -t 2024-06-01T00:00:00 -T 2024-06-01T23:00:00 --minimum-latitude 0 --maximum-latitude 65 --minimum-longitude -110 --maximum-longitude 0
```


## About the dataset- which one to download?
- hourly available dataset: `cmems_mod_glo_phy_anfc_0.083deg_PT1H-m` is only **after 2022/06**
- Before 2022/06, you have to [pick daily mean](https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/services):
  1. `cmems_mod_glo_phy_my_0.083deg_P1D-m`
  2. `cmems_mod_glo_phy_myint_0.083deg_P1D-m`

Choice 2 (`int`) covers an interim period (not sure what exactly that mean!), but it is available from 2021/07- 2024/07, for which we already downloaded hourly, therefore this `int` can be ignored!

Since choice 1 (`cmems_mod_glo_phy_my_0.083deg_P1D-m`) includes 3d and 2d fields, we'll have to subset carefully to limit file size.

`2021/06- 2021/12`: For 2021/06: use `cmems_mod_glo_phy_my_0.083deg_P1D-m` and thereafter for rest of 2021, use: `cmems_mod_glo_phy_myint_0.083deg_P1D-m`

Before 2021: use `cmems_mod_glo_phy_my_0.083deg_P1D-m`.

### Download 2021:
- 2021/06:

```
copernicusmarine subset -i cmems_mod_glo_phy_my_0.083deg_P1D-m --credentials-file ~santa/ -o ./glorys12 -t 2021-07-01T00:00:00 -T 2021-12-01T23:00:00 --minimum-latitude 0 --maximum-latitude 65 --minimum-longitude -110 --maximum-longitude 0 -z 0 -Z 0 -v zos -v thetao -v so -v uo -v vo
```

- 2021/07- 2021/12:
```
copernicusmarine subset -i cmems_mod_glo_phy_myint_0.083deg_P1D-m --credentials-file ~santa/ -o ./glorys12 -t 2021-07-01T00:00:00 -T 2021-12-31T23:00:00 --minimum-latitude 0 --maximum-latitude 65 --minimum-longitude -110 --maximum-longitude 0 -z 0 -Z 0 -v zos -v thetao -v so -v uo -v vo
```

- Follow :arrow_up: for years before 2021.


# Note:
The `CLI` works only on hercules. Why? Maybe because that's where I installed the toolbox and hence will not work on Orion.
