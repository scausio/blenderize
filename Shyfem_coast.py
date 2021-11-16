import os
import numpy as np




class Coast():
    def __init__(self,path):
        self.read(path)


    def untilEmtpyLine(self, data):
        while True:
            line = next(data)
            if line == "" or (line[:-1].strip() == ""):
                return
            yield line

    def readEdges(self,data):
        lines = []
        while True:
            try:
                head = next(data)
                line = list(self.untilEmtpyLine(data))
                lines.append([int(node)  for row in line for node in row.split()][:-1])
            except:
                return lines


    def read(self,path):
        coast = open(path)
        self.nodes = np.loadtxt(self.untilEmtpyLine(coast))[:,[1,3,4]]
        idNodes = self.nodes[:, 0]
        self.nodes=self.nodes[:,-2:]
        print (self.nodes.shape)
        outshape=np.array(self.nodes.shape)
        outshape[-1]+=1
        z=np.zeros(outshape)
        z[:,:-1]=self.nodes
        self.nodes=z
        nodeSorter = np.argsort(idNodes)

        edges=[]
        for line in self.readEdges(coast):
            for li in zip(line[:-1],line[1:]):
                edges.append(li)

        edgesIds = np.array(edges)
        self.edges = nodeSorter[idNodes.searchsorted(edgesIds, sorter=nodeSorter)]



def main():
    path='/Users/scausio/Desktop/condivisa_VM/sav_coast.file_path'
    c=Coast(path)
    print (c.edges)




if __name__ == '__main__':
    main()
