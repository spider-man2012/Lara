
"""The A* algorithm is a smart way to find the shortest path in a graph or grid. It combines the cost to get to a node with an estimate of how much more it will cost to reach the goal, helping it make informed decisions about where to explore next.

Here’s how it works:

Start by setting up a few things: an open list (where you keep track of nodes to explore), a closed list (for nodes you’ve already visited), and make sure the cost to reach the starting node (the g-value) is set to 0.

Calculate an estimate (the h-value) for each node using a heuristic function. This function helps guess how far each node is from the goal. Common methods for this include using the Euclidean distance or Manhattan distance.

Add the starting node to the open list, using its total cost (the f-value, which is the sum of g-value and h-value) to prioritize it.

Now, you’re ready to explore! Keep going until the open list is empty or you find your goal:

Remove the node with the lowest f-value from the open list. This becomes your current node.
If the current node is the goal, you’ve made it! The algorithm stops here, and you have your path.
If not, add the current node to the closed list so you don’t revisit it.
Next, look at all the neighboring nodes of your current node:
Calculate the tentative g-value for each neighbor by adding the cost to reach that neighbor to the g-value of your current node.
If the neighbor isn’t in the closed list or if the new g-value is lower than its current one:
Update its g-value.
Calculate the new f-value by adding its g-value and h-value.
If it’s not already in the open list, add it with its new f-value.
If it is in the open list, update its priority if the new f-value is lower.
Set the current node as the parent of the neighbor, keeping track of how you got there.
If you empty the open list without finding the goal, that means there’s no available path.

Once you reach the goal, you can trace back your steps by following the parent pointers from the goal node back to the start to reconstruct your path.


"""

import heapq
romania_map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}

}

class Node:
    def __init__(self, city, cost, parent=None):
        self.city = city
        self.cost = cost
        self.parent = parent
    
    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(node, goal):
    return 0  # No need for heuristic in this case

def astar_search(graph, start, goal):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.city == goal.city:
            path = []
            while current_node:
                path.append(current_node.city)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get it from start to goal
        
        closed_set.add(current_node.city)

        for neighbor, distance in graph[current_node.city].items():
            if neighbor not in closed_set:
                new_cost = current_node.cost + distance
                new_node = Node(neighbor, new_cost, current_node)
                heapq.heappush(open_list, new_node)
    
    return None  # No path found

start_city = 'Arad'
goal_city = 'Bucharest'

start_node = Node(start_city,0)
goal_node = Node(goal_city,0)

path=astar_search(romania_map,start_node,goal_node)
if path:
    print("Path Found :",path)
else:
    print("No Path Found")