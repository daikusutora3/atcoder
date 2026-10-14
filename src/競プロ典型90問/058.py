N, K = map(int, input().split())
LOGK = 61
MAXN = 10**5
doubling = [[0 for i in range(MAXN)] for k in range(LOGK + 1)]


def calc_y(x):
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
    return res


def calc_z(x, y):
    return (x + y) % 10**5


def x_to_z(x):
    y = calc_y(x)
    z = calc_z(x, y)
    return z


for i in range(MAXN):
    doubling[0][i] = x_to_z(i)

for k in range(LOGK):
    for i in range(MAXN):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]

now = N

for k in range(LOGK):
    if K >> k & 1:
        now = doubling[k][now]

print(now)
