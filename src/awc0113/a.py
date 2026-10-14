N, M = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for _ in range(M):
    ans = 0
    C = list(map(int, input().split()))[1:]
    for c in C:
        ans += P[c - 1] - Q[c - 1]
    print(ans)
