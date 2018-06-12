# cclmpyplot
An automated python plotting tool for COSMO-CLM regional climate model netcdf format outputs in curvilinear grid. 
- the program assumes that the netcdf files contain rotated grids (rlon, rlat) 
- if they do not contain such informations you could use nco to write these informations from another file: 
- To make coordinates correct again do for example: 

  ```shell
  ncatted –h -a coordinates,T_2M,c,c,"lon lat" T_2M_mm.nc

  ```
  (the coordinates attribute is created) 
  and 
  
  ```bash 
  ncks -A -v lat,lon T_2M_ts.nc T_2M_mm.nc 
  ```
  (the correct lat, lonvalues are appended from a file that includes these variables)

