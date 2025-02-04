def dfs(maze, start, goal):
    stack = [start]  # Stack for DFS
    visited = set()  # Track visited nodes
    parent = {start: None}  # To reconstruct the path

    while stack:
        x, y = stack.pop()
        if (x, y) == goal:
            break  # Goal found

        if (x, y) in visited:
            continue  # Skip visited nodes

        visited.add((x, y))

        # Possible moves: right, left, down, up
        moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in moves:
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and (nx, ny) not in visited and maze[ny][nx] == 0:  # Valid move
                stack.append((nx, ny))
                parent[(nx, ny)] = (x, y)

    # Reconstruct path
    path = []
    step = goal
    while step:
        path.append(step)
        step = parent.get(step)
    return path[::-1]  # Reverse path


# Example Maze (0 = open path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = dfs(maze, start, goal)
print("DFS Path:", path)
