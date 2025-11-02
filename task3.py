def display_results(mst, total_cost, node_map):
    print("\n--- Minimum Cost Power Grid Connections ---")
    for u, v, w in mst:
        print(f"Connect: {node_map[u]} <--> {node_map[v]} (Cost: {w})")
    print("------------------------------------------")
    print(f"Total Minimum Cost: {total_cost}")