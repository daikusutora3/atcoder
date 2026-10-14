from math import lcm


N, M = map(int, input().split())
P = list(map(int, input().split()))

now = 1
for i in range(N):
    now = lcm(now, P[i])
    if now > M:
        break

if now <= M:
    print("Yes")
else:
    print("No")
