N, M = map(int, input().split())
ij = [list(map(int, input().split())) for _ in range(M)]
i, j = ij[0]
ans = []


for _ in range(1, M):
    ni, nj = ij[_]
    if i < ni:
        ans += ["D"] * (ni - i)
    else:
        ans += ["U"] * (i - ni)
    if j < nj:
        ans += ["R"] * (nj - j)
    else:
        ans += ["L"] * (j - nj)
    i, j = ni, nj

# with open("hoge.txt", "w") as o:
print(*ans, sep="\n")
