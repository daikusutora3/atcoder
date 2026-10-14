N, K = map(int, input().split())
T = list(map(int, input().split()))
T.sort()

group = []
ans = 1
for i in range(N):
    if len(group) == 0 or T[i] - group[0] <= K:
        group.append(T[i])
    else:
        group = [T[i]]
        ans += 1

print(ans)
