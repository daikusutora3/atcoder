import bisect

N = int(input())
P = list(map(int, input().split()))

ans = 0
LIS = [P[0]]
for i in range(len(P)):
    if P[i] > LIS[-1]:
        LIS.append(P[i])
    else:
        LIS[bisect.bisect_left(LIS, P[i])] = P[i]

ans += len(LIS)


P2 = []
s = set(LIS)

for p in P:
    if p not in s:
        P2.append(p)
if len(P2):
    LIS = [P2[0]]
    for i in range(len(P2)):
        if P2[i] > LIS[-1]:
            LIS.append(P2[i])
        else:
            LIS[bisect.bisect_left(LIS, P2[i])] = P2[i]
    ans += len(LIS)

print(ans)
