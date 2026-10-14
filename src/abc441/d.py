from collections import deque

N, M, L, S, T = map(int, input().split())
g = [[] for i in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    g[u - 1].append([v - 1, c])

# (現在の頂点, 今まで辺を通った数, 今までのwalkのcost)
queue = deque([(0, 0, 0)])
ans = set()
while queue:
    u, walk, cost = queue.popleft()
    if walk == L:
        if S <= cost and cost <= T:
            ans.add(u + 1)
        continue
    elif walk > L or T < cost:
        continue

    for v, c in g[u]:
        queue.append((v, walk + 1, cost + c))
print(*sorted(list(ans)))
