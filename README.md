# blenderize

The tool allows to load SHYFEM grid, WW3 grid, HDF5, XYZ, unstructured netCDF (SHYFEM and WW3), regular netCDF files on blender.

## installation

Please copy the package in your blender directory:
*../your/path/to/Blender/blender.app/Contents/Resources/2.79/scripts/addons*

If you don't have them,  you have to install in your Blender python some python packages:
- first of all, install pip, then pip install {package}
- xarray
- netCF4
- natsort
- scipy
- h5py
- matplotlib

## load file
copy and paste in python console:

*from blenderize.blenderizator import  BlenderGrid

filepath= "path/to/file/filename.ext"
grid=BlenderGrid('nameForTheBlenderObject', filepath, 'specifierForFiletype')*

- nameForTheBlenderObject is a string, this is the name for the object in blender and for the output
- filepath is the path to the file
- specifierForFiletype is a string. Available options are:
    -- shyfem_bathy, to load a shyfem grd with bathymetry (to modify the bathy)
    -- hdf5, to load hdf5
    -- npz, to load a numpy object with keys: 'v' (for vertices [x,y,z]*N, 't' (for vertices connectivity[v1,v2,v3]*T))
    -- shyfem_grid, to load a shyfem grd without bathymetry (to modify the grid)
    -- nc_unstruct, to load a nc with bathymetry (to modify the bathy)
    -- nc_regular, to load a nc with bathymetry (to modify the bathy)
    -- xyz, text file X, Y, Z
    -- shyfem_coast, to load a shyfem coastline
    -- ww3, to load a ww3 grd with or without bathymetry (to modify the grid or and bathymetry)

BlenderGrid has 2 additional arguments that you can modify
*grid=BlenderGrid('nameForTheBlenderObject', filepath, 'specifierForFiletype',bathyCoeff=1, fillValue=False)*

bathyCoeff is a float. you can use to scale bathymentry in the visualization, all the coordinates are considered in degree
fillValue is False as default. You can need to specify a fillvalue to mask specific values. This can be helpful working on regular netcdf

##  save output

*grid.save()*



# Examples
from blenderize.blenderizator import  BlenderGrid
filepath= "/Users/scausio/Desktop/condivisa_VM/sav_coast.grd"
grid=BlenderGrid('ssaavv_coast', filepath, 'shyfem_coast')

from blenderize.blenderizator import  BlenderGrid
filepath = "/Users/scausio/Dropbox (CMCC)/PycharmProjects/bathy_tools/bathymetry_merging/savannah2021/SavannahV2_20210813_dev.grd"
grid=BlenderGrid('ssaavv', filepath,  'shyfem_grid')

from blenderize.blenderizator import  BlenderGrid
path_to_grd= "/Users/scausio/Dropbox (CMCC)/PycharmProjects/operandum/data/EMR_v1/name_msh.npz"
grid=BlenderGrid('err', path_to_grd, 'npz')

from blenderize.blenderizator import  BlenderGrid
f= '/Users/scausio/PycharmProjects/grid/ofanto201910/data/goro_z_ts.nc'
grid=BlenderGrid('goronc',f,'nc_unstruct')

from blenderize.blenderizator import  BlenderGrid
path_to_grd= "/Users/scausio/Dropbox (CMCC)/PycharmProjects/bathy_tools/bathymetry_merging/blacksea_20200513/mg_regrid.nc"
bathyCoeff=0.001
fillValue=-10
grid=BlenderGrid('bs_mask', path_to_grd, 'nc_regular',bathyCoeff,fillValue)

