from bisect import bisect_left, bisect_right


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()
ans = []
for _ in range(Q):
    b = int(input())
    bl = bisect_left(A, b)
    br = bisect_right(A, b)
    res = 10**10
    for i in set({bl, bl + 1, br - 1, br}):
        if 0 <= i < N:
            res = min(res, abs(b - A[i]))
    ans.append(res)

print(*ans, sep="\n")
