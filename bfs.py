from queue import PriorityQueue
def best_first_search(actual_Src, target, n)
    if target = n
        print(Path not found)
        return

    visited = [False]  n
    pq = PriorityQueue()
    pq.put((0, actual_Src))  
    visited[actual_Src] = True
    parent = [-1]  n  

    while not pq.empty()
        _, u = pq.get()
        if u == target
            break

        for v, _ in graph[u]
            if not visited[v]
                visited[v] = True
                parent[v] = u
                pq.put((0, v))  
    path = []
    while target != -1
        path.append(target)
        target = parent[target]
    if path[-1] != actual_Src
        print(Path not found)
    else
        print( - .join(map(str, path[-1])))

def addedge(x, y, cost)
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def main()
    global graph
    v = int(input(Enter the number of vertices ))
    graph = [[] for _ in range(v)]

    e = int(input(Enter the number of edges ))
    print(Enter each edge in the format (source destination cost))
    for _ in range(e)
        x, y, cost = map(int, input().split())
        addedge(x, y, cost)

    source = int(input(Enter the source vertex ))
    target = int(input(Enter the target vertex ))
    print(Path from source to target)
    best_first_search(source, target, v)

if __name__ == __main__
    main()
