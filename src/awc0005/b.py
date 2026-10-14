N, M, K = map(int, input().split())
S = list(map(int, input().split()))
for _ in range(M):
    p, v = map(int, input().split())
    S[p - 1] = v

print(sum([1 if S[i] < K else 0 for i in range(N)]))
