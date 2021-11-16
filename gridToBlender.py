from blenderize.blenderizator import  BlenderGrid

grd='/Users/scausio/Documents/data/grids/ofanto20190529/ofantoNoCatch.file_path'
box=[[-180,180],[ -90,90]]
bathyCoeff=-0.0001
grid=BlenderGrid('onoCatch',grd,bathyCoeff,'file_path',box)
# otranto
#file_path='/Users/scausio/Desktop/SANIv2_grid/saniv2l5.file_path'
#box=[[18.49,18.59],[42.36,42.4]]


# marmara
#file_path='/Users/scausio/Desktop/SANIv2_grid/umedbs/atl_Umed_hmin5.file_path'
#box=[[25.6,30],[39.5,41.6]]

#BlenderGrid(objName, file ,bathyCoeff, dataType, box





#grid= ShyfemGrid(file_path, box)
#grid.inBox()
#print grid.msk.shape, grid.triangsArray.shape
#v,t=grid.boxToNumpy(os.path.join('t','box.npz'))
#grid=BlenderGrid('transmarmara',file_path,box)
# save newgrid
#grid.write()


'''
#        LOAD GRID
from blenderize.blenderizator import  BlenderGrid,sortEdges
import numpy as np

file_path='/Users/scausio/Desktop/SANIv2_grid/umedbs/atl_Umed_hmin5.file_path'
box=[[25.6,30],[39.5,41.6]]
grid=BlenderGrid('transmarmara',file_path,box)

#         LOAD SELECTION FROM ARRAY
f='/Users/scausio/Desktop/SANIv2_grid/umedbs/trans_msk.npy'
selection=np.load(f)

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
bpy.ops.object.select_all(action='DESELECT')
mesh = bpy.context.object.data

for e , sel in zip (mesh.edges,selection):
    e.select=sel

bpy.ops.object.mode_set(mode = 'EDIT')

#        EXPORT SELECTED VERTICES AS ARRAY
selected_edges = [e for e in mesh.edges if e.select]
selected_nodes = [n for n in mesh.vertices if n.select]
selected_nodesId = np.array([tuple((i.vertices[0], i.vertices[1])) for i in selected_edges]) # GET ID
selected_nodesCo=[mesh.vertices[i].co.xy for i in selected_nodesId.flatten()]  #     GET COORDS

n=sortEdges(selected_nodesId)   # GET ORDERED NODES
np.save('/Users/scausio/Desktop/SANIv2_grid/umedbs/sortId',n)
nsortCo=[mesh.vertices[i].co.xy for i in n]

np.save('/Users/scausio/Desktop/SANIv2_grid/umedbs/sortCo',nsortCo)
np.save('/Users/scausio/Desktop/SANIv2_grid/umedbs/transectCo',selected_nodesCo)

'''
'''
# APPLY COLORS TO VERTEX

import bmesh

bm = bmesh.new()
bm.from_mesh(mesh)

color_layer = bm.loops.layers.color.new("color")

colors=np.load('/Users/scausio/Desktop/SANIv2_grid/umedbs/salinity.npy').tolist()

for face in bm.faces:
    for loop in face.loops:
        print("Vert:", loop.vert.index)
        loop[color_layer] = colors[loop.vert.index]
        print(loop[color_layer])
bm.to_mesh(mesh) 

'''



















'''import bpy
obj = bpy.context.object
mesh = obj.data
obj.update_from_editmode() # Loads edit-mode data into object data

selected_polygons = [p for p in mesh.polygons if p.select]
selected_edges = [e for e in mesh.vertices if e.select]
selected_vertices = [v for v in mesh.vertices if v.select] # to get all
selected_vertices = [v.co for v in mesh.vertices if v.select] # to get coords
b= [v.index for v in mesh.vertices if v.select] # to get index
v = [True  if v.select else False for v in mesh.vertices ]
np.save('/Users/scausio/Desktop/SANIv2_grid/umedbs/transectMsk',v)


transectPath='/Users/scausio/Desktop/SANIv2_grid/umedbs/transCoords.npy'
lon,lat=np.load(transectPath).T


plt.scatter(lon,lat)
plt.show()
'''
