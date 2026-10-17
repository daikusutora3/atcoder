from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))

rui = [0 for i in range(N + 1)]
for i in range(N):
    rui[i + 1] += rui[i] + A[i]

ruirui = [0 for i in range(N + 1)]
for i in range(N):
    ruirui[i + 1] += ruirui[i] + rui[i + 1]

C = [0 for i in range(N + 1)]
for i in range(N):
    C[i + 1] += C[i] + i + 1


def solve(x):
    global rui, C, N
    res = 0
    bl = bisect_left(C, x)
    # 完全にxまでで含まれてる連結された配列
    res += ruirui[bl]
    if C[bl] == x:
        return res
    # はみ出したところを足す
    res -= rui[bl] - rui[x - C[bl - 1]]
    # print("!", x, bl, res)
    return res


for _ in range(Q):
    L, R = map(int, input().split())
    print(solve(R) - solve(L - 1))
