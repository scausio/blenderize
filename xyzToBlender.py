import numpy as np
from scipy.spatial.qhull import Delaunay
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import os


class xyz():
    def __init__(self, Path, bathyCoeff, box):
        self.path = Path
        self.box = box
        self.bathyCoeff = bathyCoeff
        self.readFile()

    def readFile(self):

        self.points = np.load(self.path).T
        print (self.points.shape)
        self.lon = self.points[:,0]
        self.lat =self.points[:,1]
        self.depth = self.points[:,2]


    def inBox(self):

        self.msk = (
            (self.points[:, 0] >= self.box[0][0]) &
            (self.points[:, 0] <= self.box[0][1]) &
            (self.points[:, 1] >= self.box[1][0]) &
            (self.points[:, 1] <= self.box[1][1]))

        self.pointsInBox = self.points[self.msk]

        self.latitude = self.pointsInBox[:, 1]
        self.longitude = self.pointsInBox[:, 0]
        self.depth = self.pointsInBox[:, 2]

    def triangulateElems(self):
        self.inBox()
        tri = Delaunay(np.vstack((self.longitude, self.latitude)).T)
        self.tri = tri.simplices.copy()

    def boxToNumpy(self, outfile):
        self.triangulateElems()
        np.savez(outfile, v=np.array((self.longitude, self.latitude, self.depth * -self.bathyCoeff)).T, t=self.tri)
        return np.array((self.longitude, self.latitude, self.depth * -self.bathyCoeff)).T, self.tri

    def saveHdf5(self, outPath):
        if not os.path.exists(outPath):
            os.makedirs(outPath)
        with open(os.path.join(outPath, 'newGrd.file_path'), 'w') as outfile:
            filenames = ['nodes.txt', 'elems.txt']
            np.savetxt(os.path.join(outPath, 'nodes.txt'), self.nodes, fmt='%i %i %i %f %f')
            np.savetxt(os.path.join(outPath, 'elems.txt'), self.elems, fmt='%i %i %i %i %i %i %i %.1f')
            for fname in filenames:
                with open(os.path.join(outPath, fname)) as infile:
                    for line in infile:
                        outfile.write(line)
            for f in filenames:
                os.remove(os.path.join(outPath, f))


