from math import lcm


N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for bit in range(1, 2**K):
    l = []
    for k in range(K):
        if bit >> k & 1:
            l.append(V[k])
    ans += ((-1) ** (len(l) + 1)) * (N // lcm(*l))

print(ans)
