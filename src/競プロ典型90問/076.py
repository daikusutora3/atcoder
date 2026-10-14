from bisect import bisect_left


N = int(input())
A = list(map(int, input().split())) * 2
ruiA = [0 for i in range(2 * N + 1)]

for i in range(2 * N):
    ruiA[i + 1] = ruiA[i] + A[i]

su = ruiA[N] - ruiA[0]
ans = False
for i in range(N):
    bl = bisect_left(ruiA, (su // 10) + ruiA[i])
    if su // 10 == ruiA[bl] - ruiA[i]:
        ans = True

print("Yes" if ans and su % 10 == 0 else "No")
