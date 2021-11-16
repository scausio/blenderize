def sortEdges(edges):
    """
    generate a connected sequence of nodes from connected couples
    :param edges: an iterable of couple of hashable nodes
    :return: a list of continuosly connected nodes (random direction)
    """
    edgesIndex = {}
    print "indexing"
    for edge in edges:
        a, b = edge
        edgesIndex.setdefault(a, []).append(b)
        edgesIndex.setdefault(b, []).append(a)
    print "ok"
    print "search for head"
    for k, v in edgesIndex.items():
        if len(v) == 1:
            head = k
            break
    segment = [head, edgesIndex[head][0]]
    print "forward"
    nextVertex = [v for v in edgesIndex.get(segment[-1]) if v != segment[-2]]
    while len(nextVertex) > 0:
        segment.append(nextVertex[0])
        nextVertex = [v for v in edgesIndex.get(segment[-1]) if v != segment[-2]]
    return segment




