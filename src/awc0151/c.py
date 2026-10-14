from collections import deque

N, V, Q = map(int, input().split())
TW = deque([list(map(int, input().split())) for i in range(N)])

query = []
for i in range(Q):
    X = int(input())
    query.append((X, i))

query.sort()

ans = [0 for i in range(Q)]

now = 0
time = 0
w = 0

for X, qi in query:
    while len(TW) and TW[0][0] <= X:
        now += (
            (1 if w != 0 else 0)
            * (1 if w >= 0 else -1)
            * (abs(w) + V)
            * (TW[0][0] - time)
        )
        time = TW[0][0]
        w = TW[0][1]
        TW.popleft()

    now += (1 if w != 0 else 0) * (1 if w >= 0 else -1) * (abs(w) + V) * (X - time)
    time = X
    ans[qi] = now

for a in ans:
    print(a)
