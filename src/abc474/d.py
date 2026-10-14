N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

now = 0
ans = []


for i in range(N):
    if A[i] > B[i]:
        ans.append(10**18)
        now += (10**18) * (A[i] - B[i])
    else:
        ans.append(1)
        now -= (1) * (B[i] - A[i])


if now > 0:
    print("Yes")
    print(*ans)
else:
    print("No")
