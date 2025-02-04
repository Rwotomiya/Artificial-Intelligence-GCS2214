# Define the Depth-First Search (DFS) function to find a path in a maze
def dfs(maze, start, goal):
    # Initialize a stack with the starting position for DFS
    stack = [start]

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Initialize a dictionary to keep track of parent nodes for path reconstruction
    parent = {start: None}

    # Loop until the stack is empty
    while stack:
        # Pop the last element from the stack (DFS behavior)
        x, y = stack.pop()

        # Check if the current position is the goal
        if (x, y) == goal:
            break  # Exit the loop if the goal is found

        # Skip if the current position has already been visited
        if (x, y) in visited:
            continue

        # Mark the current position as visited
        visited.add((x, y))

        # Define possible moves: right, left, down, up
        moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        # Iterate through each possible move
        for nx, ny in moves:
            # Check if the move is within the maze boundaries and not a wall
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and (nx, ny) not in visited and maze[ny][nx] == 0:
                # Add the valid move to the stack
                stack.append((nx, ny))
                # Record the parent of the current move for path reconstruction
                parent[(nx, ny)] = (x, y)

    # Reconstruct the path from goal to start
    path = []
    step = goal

    # Trace back from the goal to the start using the parent dictionary
    while step:
        path.append(step)
        step = parent.get(step)

    # Return the path in reverse order (from start to goal)
    return path[::-1]

# Example maze representation (0 = open path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Define the start and goal positions
start = (0, 0)
goal = (4, 4)

# Call the DFS function to find the path from start to goal
path = dfs(maze, start, goal)

# Print the resulting path
print("DFS Path:", path)
