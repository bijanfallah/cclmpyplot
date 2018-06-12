<div align="center">
  <img src="http://users.met.fu-berlin.de/~BijanFallah/rain_bijan.png"><br><br>
</div>

-----------------

**CclmPyPlot**


An automated python plotting tool for [COSMO-CLM](https://www.clm-community.eu/)  regional climate model netcdf format outputs in curvilinear grid. 
- the program assumes that the netcdf files contain rotated grids (rlon, rlat) 
- if they do not contain such informations you could use nco to write these informations from another file: 
- To make coordinates correct again do for example: 

  ```shell
  ncatted –h -a coordinates,T_2M,c,c,"rlon rlat" T_2M_mm.nc

  ```
  (the coordinates attribute is created) 
  and 
  
  ```bash 
  ncks -A -v rlat,rlon T_2M_ts.nc T_2M_mm.nc 
  ```
  (the correct lat, lon values are appended from a file that includes these variables). Here we assume that the T_2M_ts.nc contains rlat and rlon values.
 ## packages
 
 - cartopy 
 - netcdf-bin
 - NETCDF4
 ## test case video :
 
 
 


<a href="http://www.youtube.com/watch?feature=player_embedded&v=RfOZD68FwXs
" target="_blank"><img src="http://img.youtube.com/vi/RfOZD68FwXs/0.jpg" 
alt="cclm python plot" width="240" height="180" border="10" /></a>
