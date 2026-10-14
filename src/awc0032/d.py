N, M = map(int, input().split())
A = list(map(int, input().split()))
D = list(map(int, input().split()))
A.sort(reverse=True)
D.sort(reverse=True)
ans = 0
flag = True

for i in range(M):
    if A[i] - D[i] < 0:
        flag = False
        break
    ans += A[i] - D[i]


print(ans if flag else -1)
