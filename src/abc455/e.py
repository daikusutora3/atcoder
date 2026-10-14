N = int(input())
S = input()
Ar = [0 for i in range(N + 1)]
Br = [0 for i in range(N + 1)]
Cr = [0 for i in range(N + 1)]
for i, s in enumerate(S):
    Ar[i + 1] += Ar[i] + (1 if s == "A" else 0)
    Br[i + 1] += Br[i] + (1 if s == "B" else 0)
    Cr[i + 1] += Cr[i] + (1 if s == "C" else 0)

ABr = [Ar[i] - Br[i] for i in range(N + 1)]
BCr = [Cr[i] - Br[i] for i in range(N + 1)]
ACr = [Ar[i] - Cr[i] for i in range(N + 1)]


ABd = [set() for i in range(N + 1)]
BCd = [set() for i in range(N + 1)]
ACd = [set() for i in range(N + 1)]

for i in range(N + 1):
    ABd[ABr[i]].add(i)
    BCd[BCr[i]].add(i)
    ACd[ACr[i]].add(i)

ans = 0
for l in range(N + 1):
    ABd[ABr[l]].remove(l)
    BCd[BCr[l]].remove(l)
    ACd[ACr[l]].remove(l)
    s = ABd[ABr[l]] | BCd[BCr[l]] | ACd[ACr[l]]
    ans += len(s)

print(N * (N + 1) // 2 - ans)
