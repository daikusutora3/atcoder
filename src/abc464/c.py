from collections import defaultdict, deque


N, M = map(int, input().split())


ADB = []
d = defaultdict(int)
for _ in range(N):
    A, D, B = map(int, input().split())
    d[A] += 1
    ADB.append((A, D, B))

ADB.sort(key=lambda x: x[1])
ADB = deque(ADB)

cnt = 0
for m in range(1, M + 1):
    while len(ADB) and ADB[0][1] <= m:
        A, D, B = ADB.popleft()
        d[A] -= 1
        d[B] += 1
        if d[A] == 0:
            del d[A]
    print(len(d.keys()))
