from collections import defaultdict, deque


H, W, N = map(int, input().split())
r2c = defaultdict(list)
c2r = defaultdict(list)

for _ in range(N):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    r2c[r].append(c)
    c2r[c].append(r)

queue = deque([(0, 0)])
dist = [[float("inf") for j in range(W)] for i in range(H)]
dist[0][0] = 0

while len(queue):
    i, j = queue.popleft()
    Ui = -1
    Di = H
    Lj = -1
    Rj = W
    for r in c2r[j]:
        if r < i:
            Ui = max(Ui, r)
        if r > i:
            Di = min(Di, r)
    for c in r2c[i]:
        if c < j:
            Lj = max(Lj, c)
        if c > j:
            Rj = min(Rj, c)
    for ni, nj in [(Ui + 1, j), (Di - 1, j), (i, Lj + 1), (i, Rj - 1)]:
        if dist[ni][nj] > dist[i][j] + 1:
            dist[ni][nj] = dist[i][j] + 1
            queue.append((ni, nj))

print(-1 if dist[H - 1][W - 1] == float("inf") else dist[H - 1][W - 1])
