N = int(input())
S = input()
s = set()
suf = 0
for i in range(N - 1, 0, -1):
    s.add(S[i])
    if len(s) == 3:
        suf = i
        break
s = set()
pref = 0
for i in range(N):
    s.add(S[i])
    if len(s) == 3:
        pref = i
        break

A = [0 for i in range(N + 1)]
B = [0 for i in range(N + 1)]
C = [0 for i in range(N + 1)]

for i in range(N):
    A[i + 1] += A[i] + (1 if S[i] == "A" else 0)
    B[i + 1] += B[i] + (1 if S[i] == "B" else 0)
    C[i + 1] += C[i] + (1 if S[i] == "C" else 0)


def is_ok(s, k):
    return A[k] - A[s] > 0 and B[k] - B[s] > 0 and C[k] - C[s] > 0


ans = 0
for i in range(pref + 1, N - 1):
    ok = N
    ng = i
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(i, mid):
            ok = mid
        else:
            ng = mid
    ans += max(0, suf - ok + 1)

print(ans)
