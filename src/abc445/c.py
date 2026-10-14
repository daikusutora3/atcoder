from collections import defaultdict, deque


N = int(input())
A = list(map(int, input().split()))
ans = defaultdict(lambda: -1)
for s in range(N):
    if ans[s] != -1:
        continue
    queue = deque([s])
    memo = set({s})
    tmp = 0
    while queue:
        i = queue.popleft()
        ni = A[i] - 1
        if ni not in memo:
            memo.add(A[i] - 1)
            queue.append(A[i] - 1)
        else:
            tmp = i
    for i in memo:
        ans[i] = tmp

for s in range(N):
    print(ans[s] + 1, end=" ")
print()
