# readme

#open blender
#copy and paste in python console:

#
#from blenderize.blenderizator import  BlenderGrid,sortEdges
##import numpy as np
#bathyCoeff=0.0001
#npy='/Users/scausio/PycharmProjects/bathymetry/kkkToNumpySH.npz'
#box=[[  28.999542,41.208459],[ 29.375396,41.305151]]
#box=[[   25.451643,39.333480],[30.394785, 41.782188]]
#box = [[ 28.463687,40.652665], [30.218332,41.695858]]
#grid=BlenderGrid(' name, grd,bathyCoeff, dataType, box')



#2) modify bathymetry on blender#

#3) save grid: 

#grid.writeGrd()

#newGrd.grd is the output


If you have a regular netcdf, please convert it into npz
 using the regular_ncToBlender script.
Then load the npz  into blender, modify and 
save the depth as npy with x,y,z array using:

bpy.ops.object.mode_set(mode='OBJECT')
m = bpy.context.object.data
mesh = np.array([i.co for i in m.vertices])
mesh[:, -1]=mesh[:, -1] / - bathyCoeff

Then, run rebuildBathyBS to obtain the netcdf




from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= '/Users/scausio/PycharmProjects/grid/ofanto201910/data/goro_z_ts.nc'
box=[[ -90,90],[ -180,180]]#ofanto
bathyCoeff=-0.0001
grid=BlenderGrid('goronc',f,bathyCoeff,box,'nc')


from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= '/Users/scausio/Documents/data/ofanto/20200206/grid_noSection_0.txt'
box=[[ -90,90],[ -180,180]]#ofanto
bathyCoeff=-0.0001
grid=BlenderGrid('font',f,bathyCoeff,box,'xyz')

from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= '/Users/scausio/Desktop/ER_V2.5.bnode05m.grd'
box=[[ -90,90],[ -180,180]]#ofanto
bathyCoeff=-0.0001
grid=BlenderGrid('emr',f,bathyCoeff,box,'grd')

from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= 'Users/scausio/PycharmProjects/gblender/blenderize/ofanto_20200211.npz'
box=[[ -90,90],[ -180,180]]#ofanto
bathyCoeff=1
grid=BlenderGrid('font',f,bathyCoeff,box,'npc')


from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= '/Users/scausio/Desktop/condivisa_VM/grid_global/definitivi/global20200414.grd'
box=[[ -90,90],[ -180,180]]
bathyCoeff=1
grid=BlenderGrid('g',f,bathyCoeff,box,'grid')


from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= '/Users/scausio/Dropbox (CMCC)/PycharmProjects/bathy_tools/fiumicino_tosmooth.npz'
box=[[ -90,90],[ -180,180]]
bathyCoeff=-0.0001
grid=BlenderGrid('fium_smth',f,bathyCoeff,box,'npz')

from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= '/Users/scausio/Dropbox (CMCC)/ofanto/grids/ofanto_river_20200217_tmp.grd'
box=[[ -90,90],[ -180,180]]#ofanto
bathyCoeff=-0.0001
grid=BlenderGrid('ofn_20200929',f,bathyCoeff,box,'grd')


from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
f= '/Users/scausio/PycharmProjects/ww3_tools/gridTools/test.npz'
box=[[ -90,90],[ -180,180]]
bathyCoeff=-0.0001
grid=BlenderGrid('test',f,1,box,'npz')



from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
path_to_grd= "/Users/scausio/Dropbox (CMCC)/grids_engineering/grids/fiumicino_newHarb.grd"
box=[[ -90,90],[ -180,180]]
bathyCoeff=1
grid=BlenderGrid('fium_hb', path_to_grd, bathyCoeff,box, 'grid')


from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
path_to_grd= "/Users/scausio/Documents/data/PHD/mask_error/global_mean.nc"
box=[[ -90,90],[ -180,180]]
bathyCoeff=1
grid=BlenderGrid('bs_mask', path_to_grd, 1,box, 'nc')

from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
path_to_grd= "/Users/scausio/Dropbox (CMCC)/PycharmProjects/operandum/data/emr_final_coast.npz"
box=[[ -90,90],[ -180,180]]
bathyCoeff=1
grid=BlenderGrid('err', path_to_grd, 1,box, 'npz')

from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np
path_to_grd= "/Users/scausio/Dropbox (CMCC)/PycharmProjects/bathy_tools/bathymetry_merging/savannah2021/SavannahV2_20210813_dev.grd"
box=[[ -90,90],[ -180,180]]
bathyCoeff=1
grid=BlenderGrid('ssaavv', path_to_grd, 1,box, 'grid')

from blenderize.blenderizator import  BlenderGrid
import numpy as np
path_to_grd= "/Users/scausio/Desktop/condivisa_VM/sav_coast.grd"
box=[[ -90,90],[ -180,180]]
bathyCoeff=1
grid=BlenderGrid('ssaavv_coast', path_to_grd, 1,box, 'coast')