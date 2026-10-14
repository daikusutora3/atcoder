from collections import defaultdict


N = int(input())

ans = defaultdict(list)

for _ in range(N):
    A = list(map(int, input().split()))[1:]
    for a in A:
        ans[a].append(_ + 1)


for i in range(1, 1 + N):
    print(len(ans[i]), *ans[i])
