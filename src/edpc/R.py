mod = 10**9 + 7


# https://qiita.com/ophhdn/items/e6451ec5983939ecbc5b
def mat_mul(a, b):
    global mod
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= mod
    return c


def mat_pow(x, n):
    y = [[0] * len(x) for _ in range(len(x))]

    for i in range(len(x)):
        y[i][i] = 1

    while n > 0:
        if n & 1:
            y = mat_mul(x, y)
        x = mat_mul(x, x)
        n >>= 1

    return y


N, K = map(int, input().split())

LOGK = 61
A = [[0 for __ in range(N)] for _ in range(N)]

for i in range(N):
    a = list(map(int, input().split()))
    A[i] = a


A = mat_pow(A, K)

ans = 0
for i in range(N):
    for j in range(N):
        ans += A[i][j]
        ans %= mod
print(ans)
