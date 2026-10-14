N, Q = map(int, input().split())
A = list(map(int, input().split()))

ruiseki = [0 for i in range(N + 1)]

for i in range(N):
    ruiseki[i + 1] += ruiseki[i] + A[i]

ans = []
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, x = map(int, query.split())
        ruiseki[x] += A[x] - A[x - 1]
        A[x - 1], A[x] = A[x], A[x - 1]
    elif query[0] == "2":
        _, l, r = map(int, query.split())
        ans.append(ruiseki[r] - ruiseki[l - 1])

print(*ans, sep="\n")
