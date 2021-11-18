import os
import numpy as np
from blenderize.shyfem import ShyfemGrid
from blenderize.hdf5ToBlender import hdf5Bathy
from blenderize.ncToBlender import NcBathy_unstruct,NcBathy_regular
from blenderize.xyzToBlender import xyz
from blenderize.Shyfem_coast import Coast
from blenderize.gmsh import GmeshMSH
from blenderize.writer import Writer
import bpy
import xarray as xr



# SORT SEGMENT
def sortEdges(edges):
    edgesIndex = {}
    for edge in edges:
        a, b = edge
        edgesIndex.setdefault(a, []).append(b)
        edgesIndex.setdefault(b, []).append(a)
    for k, v in edgesIndex.items():
        if len(v) == 1:
            head = k
            break
    segment = [head, edgesIndex[head][0]]
    nextVertex = [v for v in edgesIndex.get(segment[-1]) if v != segment[-2]]
    while len(nextVertex) > 0:
        segment.append(nextVertex[0])
        nextVertex = [v for v in edgesIndex.get(segment[-1]) if v != segment[-2]]
    return segment


class BlenderGrid():
    def __init__(self, name, file_path, dataType, bathyCoeff=1, fillValue=False):
        self.name=name
        self.file_path=file_path
        self.outPath = outPath = os.path.dirname(file_path)
        self.dataType=dataType
        self.fv=fillValue
        box=[[ -90,90],[ -180,180]]
        print (outPath)
        if not os.path.exists(outPath):
            os.makedirs(outPath)
        if dataType=='shyfem_bathy': # this triangulates centroids with Delaunay
            self.grid = ShyfemGrid(file_path, bathyCoeff, box)
            v, t = self.grid.boxToNumpy(os.path.join(outPath, 'box.npz'))
            l=[]
        elif dataType=='hdf5':
            self.grid = hdf5Bathy(file_path, bathyCoeff, box, 'hdf5')
            v, t = self.grid.boxToNumpy(os.path.join(outPath, 'box.npz'))
            l = []
        elif dataType == 'npz':
            ds = np.load(file_path)
            print (ds)
            v= ds['v']
            t=ds['t']
            l = []
        elif dataType=='shyfem_grid': # this get triangulation from file_path
            self.grid = ShyfemGrid(file_path, bathyCoeff, box)
            v, t = self.grid.triFromGrdToNumpy(os.path.join(outPath, 'box.npz'))
            l = []
        elif dataType=='nc_unstruct':
            self.grid = NcBathy_unstruct(file_path, bathyCoeff)
            v, t = self.grid.toNumpy(os.path.join(outPath, 'box.npz'))
            l = []

        elif dataType=='nc_regular':

            self.grid = NcBathy_regular(file_path, bathyCoeff,self.fv)

            v, t = self.grid.toNumpy(os.path.join(outPath, 'box.npz'))
            l = []

        elif dataType=='xyz':
            self.grid = xyz(file_path, bathyCoeff, box)
            v, t = self.grid.boxToNumpy(os.path.join(outPath, 'box.npz'))
            l = []
        elif dataType=='shyfem_coast':
            self.grid = Coast(file_path)
            v,l= self.grid.nodes, self.grid.edges
            t = []
        elif dataType == 'ww3':
            self.grid = GmeshMSH(file_path)
            v, t = self.grid.triToNumpy(os.path.join(outPath, '%s_msh.npz')%self.name)
            l = []
        else:
            print ('NOT VALID DATATYPE!\n init:  name, path, bathyCoeff, box, dataType\n datatype: shyfem_bathy, hdf5, npz, shyfem_grid, nc_unstruct,nc_regular, xyz, shyfem_coast,ww3')
            return
        self.ob = self.loadObj(self.name, v,l,t)

    def mkobj(self, name):
        me = bpy.data.meshes.new(name)
        ob = bpy.data.objects.new(name, me)
        scn = bpy.context.scene
        scn.objects.link(ob)
        scn.objects.active = ob
        ob.select = True
        return ob

    def loadObj(self, name, v, l, t):
        ob = self.mkobj(name)
        if v.shape[1]==2:
            v=  np.array((v.T[0],v.T[1],np.zeros_like(v.T[0]))).T
        try:
            v=v.tolist()
        except:
            pass
        try:
            l=l.tolist()
        except:
            pass
        try:
            t=t.tolist()
        except:
            pass

        ob.data.from_pydata(v, l, t)
        return ob

    def selectionToMask(self):
        obj = bpy.context.object
        mesh = obj.data
        obj.update_from_editmode()  # Loads edit-mode data into object data
        msk = [1 if e.select else 0 for e in mesh.vertices]
        #np.save(os.path.join(self.outPath, '{}_mask'.format(self.name)), msk)
        xr.Dataset({'mask': (['node'], msk)},
                              coords={'node': np.arange(len(msk))}).to_netcdf(os.path.join(self.outPath,'{}_mask.nc'.format(self.name)))

    def saveSelected(self):
        obj = bpy.context.object
        mesh = obj.data
        obj.update_from_editmode()  # Loads edit-mode data into object data
        mskTrans = [True if e.select else False for e in mesh.edges]

        selected_edges = [e for e in mesh.edges if e.select]
        selected_nodesId = np.array([tuple((i.vertices[0], i.vertices[1])) for i in selected_edges])  # GET ID
        selected_nodesCo = [mesh.vertices[i].co.xy for i in selected_nodesId.flatten()]  # GET COORDS

        sortedEdges = sortEdges(selected_nodesId)  # GET ORDERED NODES
        sortedCoords = [mesh.vertices[i].co.xy for i in sortedEdges]

        np.save(os.path.join(self.outPath, '{}_transectId'.format(self.name)), sortedEdges)
        np.save(os.path.join(self.outPath, '{}_transectCo'.format(self.name)),  sortedCoords)

    def save(self):
        Writer(self).run()



