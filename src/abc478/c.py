N, K = map(int, input().split())
A = list(map(int, input().split()))
SA = sorted(A)
pref = 0
suf = 0

for i in range(N):
    if A[i] == SA[i]:
        pref += 1
    else:
        break

for i in range(N - 1, -1, -1):
    if A[i] == SA[i]:
        suf += 1
    else:
        break

if N - suf - pref <= K:
    print("Yes")
else:
    print("No")
