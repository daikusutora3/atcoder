N = int(input())
A = list(map(int, input().split()))
A.sort()

if N == 1:
    print(0)
elif N % 2 == 0:
    ans = 0
    for i in range(N):
        if i < (N - 2) // 2:
            ans -= 2 * A[i]
        elif i == (N - 2) // 2:
            ans -= A[i]
        elif i == (N - 2) // 2 + 1:
            ans += A[i]
        else:
            ans += 2 * A[i]
    print(ans)
else:
    ans1 = 0
    for i in range(N):
        if i < (N - 1) // 2:
            ans1 -= 2 * A[i]
        elif i == (N - 1) // 2:
            ans1 += A[i]
        elif i == (N - 1) // 2 + 1:
            ans1 += A[i]
        else:
            ans1 += 2 * A[i]
    ans2 = 0
    for i in range(N):
        if i < (N - 2) // 2:
            ans2 -= 2 * A[i]
        elif i == (N - 2) // 2:
            ans2 -= A[i]
        elif i == (N - 2) // 2 + 1:
            ans2 -= A[i]
        else:
            ans2 += 2 * A[i]
    print(max(ans1, ans2))
