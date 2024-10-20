from collections import deque

def bfs(graph,start):
    visited=set()
    queue=deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            #Explore neighbours 
            neighbours=graph[vertex]
            for neighbor in neighbours:
                if neighbor not in visited:
                    queue.append(neighbor)

#Example usage
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

start_vertex='A'
bfs(graph,start_vertex)