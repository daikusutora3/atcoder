N, M = map(int, input().split())
E = list(map(int, input().split()))
C = list(map(int, input().split()))

min_e = min(E)
ans = 0
for i in range(M):
    ans += min_e * C[i]

print(ans)
