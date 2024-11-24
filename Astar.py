import heapq
class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.adjacent = {}
        self.distance = float('inf')
        self.previous = None

    def __lt__(self, other):
        return self.distance < other.distance

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, cost):
        self.nodes[name] = Node(name, cost)

    def add_edge(self, start, end, weight):
        self.nodes[start].adjacent[self.nodes[end]] = weight

    def a_star(self, initial, goal):
        queue = []
        heapq.heappush(queue, self.nodes[initial])
        self.nodes[initial].distance = self.nodes[initial].cost

        while queue:
            current = heapq.heappop(queue)
            if current.name == goal:
                path = []
                total_cost = 0
                while current:
                    path.append(current.name)
                    total_cost += current.cost
                    current = current.previous
                path.reverse()
                return path, total_cost

            for adjacent, weight in current.adjacent.items():
                distance = current.distance + weight + adjacent.cost
                if distance < adjacent.distance:
                    adjacent.distance = distance
                    adjacent.previous = current
                    heapq.heappush(queue, adjacent)

        return None, None

# Example usage:
graph = Graph()
graph.add_node('A', 1)
graph.add_node('B', 2)
graph.add_node('C', 3)
graph.add_node('D', 2)
graph.add_node('E', 1)
graph.add_node('F', 3)

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 3)
graph.add_edge('C', 'F', 4)
graph.add_edge('F', 'E', 2)

initial_node = 'A'
goal_node = 'E'

path, cost = graph.a_star(initial_node, goal_node)
if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Cost: {cost}")
else:
    print("No path found")
