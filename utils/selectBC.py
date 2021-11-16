import numpy as np
import bpy


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

bpy.ops.object.mode_set(mode = 'OBJECT')
mesh = bpy.context.object.data

selected_edges = [e.vertices for e in mesh.edges if e.select]
bc= [i+1 for i in sortEdges(selected_edges)]


np.savetxt('bc.txt',bc,fmt='%i')
