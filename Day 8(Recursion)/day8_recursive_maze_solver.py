def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))
    print()


def solve_maze(maze, x, y, path):
    # Base case: reached the bottom-right corner (goal)
    if x == len(maze) - 1 and y == len(maze[0]) - 1 and maze[x][y] == 1:
        path[x][y] = 1
        return True

    # Check if current cell is valid
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1:
        # Mark this cell as part of the path
        path[x][y] = 1

        # Move right
        if solve_maze(maze, x, y + 1, path):
            return True
        # Move down
        if solve_maze(maze, x + 1, y, path):
            return True

        # Backtrack
        path[x][y] = 0
        return False

    return False


# Sample maze (1 = path, 0 = wall)
maze = [
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

# Empty path matrix
path = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

if solve_maze(maze, 0, 0, path):
    print("Path found:")
    print_maze(path)
else:
    print("No path exists.")
