from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            queue.extend(neighbors)

    return result


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}


result = bfs(graph, 'A')
print(result)
