from collections import deque

def bfs(maze, start, goal):
    queue = deque([start])
    visited = set()
    parent = {start: None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break

        if (x, y) in visited:
            continue

        visited.add((x, y))

        moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in moves:
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and (nx, ny) not in visited and maze[ny][nx] == 0:
                queue.append((nx, ny))
                parent[(nx, ny)] = (x, y)
    
    
    path = []
    step = goal
    while step:
        path.append(step)
        step = parent.get(step)
    return path[::-1]


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

bfs_path = bfs(maze, start, goal)
print("BFS Path:", bfs_path)
