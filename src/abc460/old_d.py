H, W = map(int, input().split())

bg = []
g = [input() for i in range(H)]


def flip(grid):
    h = len(grid)
    w = len(grid[0])
    n_grid = [["."] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                n_grid[i][j] = "."
            else:
                for di, dj in [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                    (1, 1),
                    (1, -1),
                    (-1, 1),
                    (-1, -1),
                ]:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < h and 0 <= nj < w):
                        continue
                    if grid[ni][nj] == "#":
                        n_grid[i][j] = "#"
    n_grid = ["".join(n_grid[i]) for i in range(h)]
    return n_grid


def print_grid(grid):
    print("=====")
    for i in range(len(grid)):
        print(grid[i])
    print("=====")
