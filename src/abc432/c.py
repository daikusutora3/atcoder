N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


def solve(target):
    flag = True
    Y_NUM = 0
    for a in A:
        left = 0
        right = 10**9 + 1
        X_NUM = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * X + (a - mid) * Y == target:
                X_NUM = mid
                break
            elif mid * X + (a - mid) * Y > target and not (mid > a):
                left = mid + 1
            else:
                right = mid - 1
        if X_NUM == -1:
            flag = False
            break
        Y_NUM += a - X_NUM
    return Y_NUM if flag else -1


A.sort()

if A[0] * Y >= A[-1] * X:
    print(solve(A[0] * Y))
else:
    print(-1)

# for a in A:
#     nums = []
#     for i in range(a + 1):
#         nums.append(i * X + (a - i) * Y)
#     print(nums)
