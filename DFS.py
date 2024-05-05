def dfs(graph, start, goal):
    visited = []  # List to store visited nodes
    visit_order = []  # List to store the order of node visits
    stack = [[start]]  # Initialize stack with start node
    while stack:
        path = stack.pop()  # Retrieve and remove the last path from the stack
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
                if node2 not in path:  # Check if adjacent node is not already in the path
                    newpath = list(path)  # Create a new path by copying the current path
                    newpath.append(node2)  # Add the adjacent node to the new path
                    stack.append(newpath)  # Add the new path to the stack for further exploration

solution, visit_order = dfs(graph, "A","G" )
print(" DFS Solution path:", solution)
print("DFS Order of node visits:", visit_order)