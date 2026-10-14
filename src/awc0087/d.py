from bisect import bisect_right


N, K = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

zero_ind = bisect_right(X, 0)
XL, XR = X[0:zero_ind], X[zero_ind:N]

XR.reverse()
XL = [-x for x in XL]


def solve(L):
    global K
    res = 0
    for i in range(0, len(L), K):
        res += L[i]
    return res * 2


print(solve(XL) + solve(XR))
