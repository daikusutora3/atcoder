N, Q = map(int, input().split())
A = list(map(int, input().split()))
rui = [0 for i in range(N + 1)]

for i in range(N):
    rui[i + 1] = rui[i] + A[i]


for i in range(Q):
    L, R = map(int, input().split())
    print(rui[R] - rui[L - 1])
