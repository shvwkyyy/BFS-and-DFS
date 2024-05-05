
# Define a breadth-first search (BFS) function to find the shortest path from start to goal in the graph
def bfs(graph, start, goal):
    visited = []  # List to store visited nodes
    visit_order = []  # List to store the order of node visits
    queue = [[start]]  # Initialize queue with start node
    while queue:
        path = queue.pop(0)  # Retrieve and remove the first path from the queue
        node = path[-1]  # Retrieve the last node from the path
        if node in visited:  # Skip node if already visited
            continue
        visited.append(node)  # Mark node as visited
        visit_order.append(node)  # Store the node visit order
        if node == goal:  # If goal node reached, return path and visit order
            return path, visit_order
        else:  # If goal not reached, explore adjacent nodes
            adjacent_nodes = graph.get(node, [])  # Get adjacent nodes of the current node
            for node2 in adjacent_nodes:  # Iterate over adjacent nodes
                new_path = path.copy()  # Create a new path by copying the current path
                new_path.append(node2)  # Add the adjacent node to the new path
                queue.append(new_path)  # Add the new path to the queue for further exploration

# Find the solution using BFS and get the order of node visits
solution, visit_order = bfs(graph, 'A', 'G')
print(f"BFS Your solution is {solution}")
print(f"BFS Order of node visits: {visit_order}")




    