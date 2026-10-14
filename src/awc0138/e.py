from collections import defaultdict

N, M, K, T = map(int, input().split())


direction = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
grid = [input() for i in range(N)]


def move_S(x, y, S):
    global grid
    if grid[x][y] == "#":
        return -1
    for s in S:
        dx, dy = direction[s]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if grid[nx][ny] == "#":
            continue
        x, y = nx, ny
    return x + y * N


def to_id(x, y):
    return x + y * N


def to_xy(a):
    return [a % N, a // N]


d = defaultdict(list)

for i in range(K):
    R, C, L, S = list(input().split())
    (
        R,
        C,
        L,
    ) = int(R), int(C), int(L)
    d[S].append([R, C, L, i])

ans = [-1 for i in range(K)]
move = [-1 for x in range(N * M)]

for S, data in d.items():
    for x in range(N):
        for y in range(M):
            id = to_id(x, y)
            move[id] = move_S(x, y, S)

    for R, C, L, qi in data:
        seen = defaultdict(int)
        q = T // L

        v = to_id(R - 1, C - 1)
        path = []

        while q > 0 and v not in seen:
            seen[v] = len(path)
            path.append(v)
            q -= 1
            v = move[v]

        cycle_start = seen[v]
        cycle_length = len(path) - cycle_start
        if q > 0:
            q %= cycle_length
            for i in range(q):
                v = move[v]
        x, y = to_xy(v)
        ans_v = move_S(x, y, S[: T % L])
        ans_x, ans_y = to_xy(ans_v)
        ans[qi] = (ans_x + 1, ans_y + 1)


for i in range(K):
    print(*ans[i])
