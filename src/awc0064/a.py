N, K = map(int, input().split())
A = list(map(int, input().split())) + [-1]
cnt = [1 if A[i] >= K and A[i + 1] < K else 0 for i in range(N)]

print(sum(cnt))
