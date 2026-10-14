N, K, M = map(int, input().split())
CV = [list(map(int, input().split())) for i in range(N)]
CV.sort(key=lambda x: -x[1])

cs = set()
rest = []
ans = []
for i in range(N):
    c, v = CV[i]
    if c not in cs and len(ans) < M:
        cs.add(c)
        ans.append(v)
    else:
        rest.append(v)

for i in range(K - M):
    ans.append(rest[i])

print(sum(ans))
