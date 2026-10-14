N, T = map(int, input().split())
H = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i in range(N):
    if H[i] <= T:
        ans += C[i]

print(ans)
