import bisect

N = int(input())
A = list(map(int, input().split()))

# 左からのLISの情報: [LISの長さ, LISの右端の値]
left_LIS = [[0, 0] for i in range(N)]

# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
LIS = [A[0]]
for i in range(len(A)):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    else:
        LIS[bisect.bisect_left(LIS, A[i])] = A[i]
    left_LIS[i] = [len(LIS), LIS[-1]]

# 右からのLISの情報: [LISの長さ, LISの左端の値]
right_LIS = [[0, 0] for i in range(N)]
A = A[::-1]
LIS = [A[0]]
for i in range(len(A)):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    else:
        LIS[bisect.bisect_left(LIS, A[i])] = A[i]
    right_LIS[N - i - 1] = [len(LIS), LIS[-1]]


ans = 0
for i in range(-1, N):
    if i == -1:
        ans = max(ans, right_LIS[i + 1][0])
    elif i == N - 1:
        ans = max(ans, left_LIS[i][0])
    else:
        res = left_LIS[i][0] + right_LIS[i + 1][0]
        if left_LIS[i][1] == right_LIS[i][1]:
            res -= 1
        ans = max(ans, res)

print(ans)
