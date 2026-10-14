import random
import sys


seed = int(sys.argv[1])
rng = random.Random(seed)

H = rng.randint(1, 5)
W = rng.randint(1, 5)
K = rng.randint(0, H * W)

grid = []
for _ in range(H):
    row = "".join(str(rng.randint(0, 1)) for _ in range(W))
    grid.append(row)

print(H, W, K)
print(*grid, sep="\n")
