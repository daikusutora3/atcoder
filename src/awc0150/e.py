N, Q, T = map(int, input().split())
A = list(map(int, input().split()))

rui = [0 for i in range(N + 1)]

for i in range(N):
    rui[i + 1] = rui[i] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    if rui[R] - rui[L - 1] > T:
        print("Yes")
    else:
        print("No")
