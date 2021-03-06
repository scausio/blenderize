import numpy as np
from scipy.spatial.qhull import Delaunay
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import os
import netCDF4 as nc

def findCoord(ds, coords):
    for coord in coords:
        if coord in ds.variables.keys():
            return coord

def getCoordsName(ds):
    lons=['longitude','lon', 'x','X']
    lats=['latitude','lat','y','Y']
    depths=['total_depth', 'depth', 'Bathy', 'Bathymetry', 'z','Z','bathy','bathymetry']
    lonName=findCoord(ds, lons)
    latName=findCoord(ds,lats)
    depthName=findCoord(ds,depths)

    return lonName,latName,depthName

class NcBathy_unstruct():
    def __init__(self, filePath, bathyCoeff):
        self.path = filePath
        self.bathyCoeff = bathyCoeff
        self.readFile()

    def readFile(self):
        ds = nc.Dataset(self.path)

        lonName, latName, depthName=getCoordsName(ds)

        self.lon= ds[lonName][:].filled()
        self.lat = ds[latName][:].filled()
        self.depth = ds[depthName][:].filled()

        try:
            self.tri = (ds['element_index'][:] - 1).filled()
        except:
            self.tri = (ds['tri'][:] - 1).filled()
        self.ds = ds

    def toNumpy(self, outfile):
        np.savez(outfile, v=np.array((self.lon, self.lat, self.depth * -self.bathyCoeff)).T, t=self.tri)
        return np.array((self.lon, self.lat, self.depth * -self.bathyCoeff)).T, self.tri


class NcBathy_regular():
    def __init__(self, filePath,bathyCoeff,fillValue):
        self.path = filePath
        self.bathyCoeff=bathyCoeff
        self.fv=fillValue
        self.regularToScatter()
    def readFile(self):
        ds = nc.Dataset(self.path)
        lonName, latName, depthName = getCoordsName(ds)
        print (ds)
        #lon = ds['nav_lon'][0].filled()
        #lat =ds['nav_lat'][:,0].filled()
        lon= ds[lonName][:].filled()
        lat = ds[latName][:].filled()
        depth = ds[depthName][:].filled()
        self.nan=np.isnan(depth).flatten()

        if self.fv:
            depth[depth==self.fv]=np.nan
        self.ds=ds
        return lon,lat,depth

    def regularToScatter(self):

        x,y,z=self.readFile()
        xx,yy=np.meshgrid(x,y)
        self.lon=xx.flatten()
        self.lat=yy.flatten()
        self.depth=z.flatten()*-self.bathyCoeff
        self.triangulate()

    def triangulate(self):
        tri = Delaunay(np.vstack((self.lon[np.logical_not(self.nan)], self.lat[np.logical_not(self.nan)])).T)
        self.tri = tri.simplices.copy()

    def toNumpy(self, outfile):
        out=np.array((self.lon, self.lat, self.depth)).T
        print (out.shape)
        np.savez(outfile, v=np.array(out), t=self.tri)
        print(out[0])
        print (self.tri.shape)
        print(self.tri[0])
        return np.array(out), self.tri

