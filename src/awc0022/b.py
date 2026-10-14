N, M, T = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if A[i] < T:
        cnt += T - A[i]

if cnt <= M:
    print(cnt)
else:
    print(-1)
