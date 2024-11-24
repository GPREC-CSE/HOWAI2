from collections import defaultdict
class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = defaultdict(list)
       
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
       
    def dfs(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node == end_node:
            return path
        for node in self.adj_list[start_node]:
            if node not in path:
                new_path = self.dfs(node, end_node, path)
                if new_path:
                    return new_path
        return None

def main():
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    graph = Graph(num_nodes)
   
    for _ in range(num_edges):
        u, v = map(int, input("Enter edges (u, v): ").split())
        graph.add_edge(u, v)
   
    start_node = int(input("Enter the starting node: "))
    end_node = int(input("Enter the ending node: "))
   
    path = graph.dfs(start_node, end_node)
    if path:
        print("Path from", start_node, "to", end_node, ":")
        print("-->".join(map(str, path)))
    else:
        print("No path found from", start_node, "to", end_node)

if __name__ == "__main__":
    main()
