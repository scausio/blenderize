import os
import bpy
import numpy as np

# save bendermesh ad file_path

bpy.ops.object.mode_set(mode='OBJECT')
m = bpy.context.object.data
mesh = np.array([i.co for i in m.vertices])   
        
x=mesh[:,0]
y=mesh[:,1]
ran=[i+1 for i,j in enumerate(x)] 
em=np.zeros_like(y)       
nodes=np.array((em+1,ran,em,x,y)).T       

tri=np.array([list(np.array(t.vertices)+1) for t in  m.polygons])
base=np.zeros(tri.shape[0])
ranE=[i+1 for i,j in enumerate(base)]

elems=np.array((base+2,ranE,base,base+3,tri[:,0],tri[:,1],tri[:,2])).T

with open('/Users/scausio/Desktop/ofanto_river20200229_20km','w')as out:
    np.savetxt(out,nodes, fmt='%i %i %i %f %f')
    np.savetxt(out, elems, fmt='%i %i %i %i %i %i %i %.1f')