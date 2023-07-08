from queue import Queue

graph = {
    'A': ['S', 'Z', 'T'],
    'Z': ['A', 'O'],
    'O': ['Z', 'S'],
    'S': ['A', 'O', 'F', 'R'],
    'T': ['A', 'L'],
    'L': ['T', 'M'],
    'M': ['L', 'D'],
    'D': ['M', 'C'],
    'C': ['D', 'R', 'P'],
    'R': ['S', 'C', 'P'],
    'F': ['S', 'B'],
    'P': ['R', 'C', 'B'],
    'B': ['F', 'P', 'G', 'U'],
    'G': ['B'],
    'U': ['B', 'V', 'H'],
    'H': ['U', 'E'],
    'E': ['H'],
    'V': ['I', 'U'],
    'I': ['V', 'N'],
    'N': ['I']
}

def bfs(source, destination):
    visited = {}
    parent = {}
    bfs_output = []
    queue = Queue()

    for city in graph.keys():
        visited[city] = False
        parent[city] = None

    source_city = source 
    visited[source_city] = True 
    queue.put(source_city)

    while not queue.empty():
        first_city = queue.get()
        bfs_output.append(first_city)

        for any_city in graph[first_city]:
            if not visited[any_city]:
                visited[any_city] = True
                parent[any_city] = first_city
                queue.put(any_city)
    
    destination_city = destination
    path = []
    
    while destination_city is not None:
        path.append(destination_city)
        destination_city = parent[destination_city]
    
    path.reverse()
    print(path)

bfs('A', 'B')


