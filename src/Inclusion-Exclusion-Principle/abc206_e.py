from math import comb


L, R = map(int, input().split())

F1 = [0] * (R + 1)
for g in range(2, R + 1):
    cnt = R // g - (L - 1) // g
    if cnt >= 2:
        F1[g] = 2 * comb(cnt, 2)

f1 = [0] * (R + 1)
for g in range(R, 1, -1):
    f1[g] = F1[g]
    for x in range(g * 2, R + 1, g):
        f1[g] -= f1[x]

A = [0] * (R + 1)
for g in range(2, R + 1):
    cnt = R // g - (L - 1) // g
    if cnt >= 2 and L <= g <= R:
        A[g] = 2 * (cnt - 1)

print(sum(f1) - sum(A))
