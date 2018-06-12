'''
An automatic code to plot COSMO-CLM outputs
The netcd file should contain the rotated grid information (rlat, rlon)
Written by Bijan Fallah (@bijan_berlin)
For feedbacks and questions contact me at https://www.linkedin.com/in/bijanfallah/
'''
# import block

import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature
import matplotlib.patches as patches
from netCDF4 import Dataset as NetCDFFile
import re
import os
import matplotlib.image as image


dir_target = input(" Enter the path to the data please (with / at the end)! : ")
file_name = input(" Enter the name of the netcdf file please! : ")


file_name = dir_target +file_name
nc = NetCDFFile(file_name)
lats = nc.variables['lat'][:]
lons = nc.variables['lon'][:]
rlat = nc.variables['rlat'][:]
rlon = nc.variables['rlon'][:]

dimension_names = []
for name, dimension in nc.dimensions.items():
    dimension_names.append(str(name))

var_names = []
for name, dimension in nc.variables.items():
    var_names.append(str(name))
    
print("\033[0;30;47m Here the list of variables within the netcdf file: \n")
print(var_names)
var = input(" Enter your variable name to be plotted:\n") 
t = nc.variables[var][:,:].squeeze()
def extract_poles(name):
    '''
    function to extract the rotated poles
    
    '''
    import os
    CMD = "ncdump -h " + name + ' > text' 
    os.system(CMD)
    import re
    with open('text', 'r') as file:
         raw = file.readlines()
        
    for line in raw :
     
        if re.search(r'rotated_pole:grid_north_pole_longitude =', line):
            print('pol_lon= '+ str(line.split("= ",1)[1][:-4]))
            pol_lon = float(line.split("= ",1)[1][:-4])
        if re.search(r'rotated_pole:grid_north_pole_latitude =', line):
            print("pol_lat= "+ str(line.split("= ",1)[1][:-4]))
            pol_lat = float(line.split("= ",1)[1][:-4])
    CMD = "rm -f text" 
    os.system(CMD)

    return pol_lon, pol_lat

color_bars = input(" Enter the colorbar format (blue to green [BuGn] or blue_white_red [bwr_r] or any other python colorbar): ")

#color_bars = "plt.cm." + color_bars
print(color_bars)
pol_lon, pol_lat = extract_poles(file_name)
if len(t.shape)>2 and t.shape[0]> 1:
    print('The variable has more than 1 level/time')
    answer = input('Shall I make a mean of all (yes or no)?')
    if answer == 'yes':
        t = np.mean(t, axis=0)
    else:
        answer = input('Shall I plot an specific level/time (1..'+ str(t.shape[0]) +")")
        t = t[int(answer),:,:].squeeze()   
        
fig = plt.figure('1')
fig.set_size_inches(14, 10)
pc = ccrs.PlateCarree()
rp = ccrs.RotatedPole(pole_longitude= pol_lon,
                      pole_latitude= pol_lat,
                      globe=ccrs.Globe(semimajor_axis=6370000,
                                       semiminor_axis=6370000))
ax = plt.axes(projection=rp)
#ax.imshow(im, aspect='auto',extent=(-50., 50., .1, .1), zorder=2)

ax.coastlines('50m', linewidth=0.8)
ax.add_feature(cartopy.feature.OCEAN,
               edgecolor='black', zorder=0,
               linewidth=0.8, alpha=.7)
ax.add_feature(cartopy.feature.LAND, zorder=0,
               linewidth=0.8, alpha=.7)
v = np.linspace(np.nanmin(t),np.nanmax(t) , 21, endpoint=True)
rlons, rlats = np.meshgrid(rlon, rlat)
cs = plt.contourf(rlons, rlats, t, cmap=color_bars, zorder=1) 
#cs = plt.contourf(lons, lats, t, v, transform=ccrs.PlateCarree(), cmap=plt.cm.BuGn)        
cb = plt.colorbar(cs)
cb.set_label(var, fontsize=20)
cb.ax.tick_params(labelsize=20)
os.system('mkdir plots')
#os.system('cd plots')
name = "./plots/" + var + '.pdf'
plt.savefig(name,bbox_inches='tight')
plt.close()
os.system('cd ../')
print(" Thanks a lot for using this code \n")
print(" Please follow and give feedback : https://www.linkedin.com/in/bijanfallah/ \n")


      
                

