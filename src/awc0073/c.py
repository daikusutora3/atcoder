from bisect import bisect_left, bisect_right


N, D = map(int, input().split())

XS = [list(map(int, input().split())) for i in range(N)]
XS.sort()
X = [x for x, s in XS]
ruiS = [0 for i in range(N + 1)]
for i in range(N):
    ruiS[i + 1] += ruiS[i] + XS[i][1]


ans = 0
for i in range(N):
    bl = max(i + 1, bisect_left(X, XS[i][0] - D))
    br = bisect_right(X, XS[i][0] + D)
    # print(i, ":", (ruiS[br] - ruiS[bl]) * XS[i][1])
    ans += (ruiS[br] - ruiS[bl]) * XS[i][1]

print(ans)
