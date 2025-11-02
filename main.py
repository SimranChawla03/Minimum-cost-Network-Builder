# -*- coding: utf-8 -*-

#  TASK 1: Kruskal's Algorithm
def kruskal(nodes, edges, uf):
    edges.sort(key=lambda x: x[2])
    mst = []
    total_cost = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            total_cost += w
    return mst, total_cost


# TASK 2: Union-Find Data Structure
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


# TASK 3: Visualization
def display_results(mst, total_cost, node_map):
    print("\n--- Minimum Cost Power Grid Connections ---")
    for u, v, w in mst:
        print(f"Connect: {node_map[u]} <--> {node_map[v]} (Cost: {w})")
    print("------------------------------------------")
    print(f"Total Minimum Cost: {total_cost}")


# MAIN PROGRAM
if __name__ == "__main__":
    node_map = {
        0: "Power Station (PS)",
        1: "Substation A",
        2: "Substation B",
        3: "Town C",
        4: "Industrial Zone D"
    }

    edges = [
        (0, 1, 4),
        (0, 2, 8),
        (1, 2, 2),
        (1, 3, 3),
        (2, 4, 9),
        (3, 4, 6),
        (2, 3, 5)
    ]

    uf = UnionFind(len(node_map)) 
    mst, total_cost = kruskal(node_map, edges, uf)
    display_results(mst, total_cost, node_map)
           