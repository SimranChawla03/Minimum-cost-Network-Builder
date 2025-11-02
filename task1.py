def kruskal(nodes, edges, uf):
    edges.sort(key=lambda x: x[2])
    mst = []
    total_cost = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total_cost += w
    return mst, total_cost