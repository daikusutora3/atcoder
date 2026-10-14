N, D, K = map(int, input().split())

cnt = [0 for i in range(N + 1)]
# K日間以上連続で来館した人は1それ以外は0
flag = [0 for i in range(N + 1)]

for _ in range(D):
    S = set(list(map(int, input().split()))[1:])
    for i in range(N + 1):
        if i in S:
            cnt[i] += 1
    for i in range(N + 1):
        if cnt[i] >= K:
            flag[i] = 1

ans = []

for i in range(N + 1):
    if flag[i]:
        ans.append(i)

if len(ans):
    print(*ans)
else:
    print(-1)
