"""
The Breadth-First Search (BFS) algorithm is a great way to explore a graph. Here’s how it works:

Start off by setting up a queue and a set to keep track of which vertices you’ve already visited.
Add the starting vertex to the queue and mark it as visited.
Keep going until the queue is empty:
Take a vertex from the front of the queue.
Do something with that vertex, like printing it out or storing it for later.
Add all of its unvisited neighbors to the queue and mark them as visited.
When the queue is empty, the algorithm is done, meaning you’ve processed all the reachable vertices."""

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