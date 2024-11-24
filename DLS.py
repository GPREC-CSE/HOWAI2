from collections import deque
def depth_limited_search(graph, start, goal, limit):
    queue = deque([(start, [start])])  
    visited = set()
   
    while queue:
        node, path = queue.popleft()
       
        if node == goal:
            return path
       
        if len(path) > limit:
            continue
       
        for neighbor in graph.get(node, []):  # Fixed loop syntax
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
   
    return None  

graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter node {i + 1}: ")
    neighbors = input(f"Enter neighbors of {node}: ")
    graph[node] = neighbors.split()
   
start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")  
depth_limit = int(input("Enter the depth limit: "))

result = depth_limited_search(graph, start_node, goal_node, depth_limit)

if result:
    print("Path found: ", "-->".join(result))  
else:
    print("No path found within the depth limit")
