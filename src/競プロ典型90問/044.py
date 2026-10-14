N, Q = map(int, input().split())
A = list(map(int, input().split()))

m = 0
for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        nx = (x - 1 + m) % N
        ny = (y - 1 + m) % N
        A[nx], A[ny] = A[ny], A[nx]
    elif T == 2:
        m = (m - 1 + N) % N
    else:
        print(A[(x - 1 + m) % N])
