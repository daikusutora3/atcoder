N, M = map(int, input().split())

W = list(map(int, input().split()))

for _ in range(M):
    A = list(map(int, input().split()))[1:]
    ans = 0
    for a in A:
        ans += W[a - 1]
    print(ans)
