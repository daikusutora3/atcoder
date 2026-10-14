import sys
from collections import defaultdict, deque

input = sys.stdin.readline
T = int(input())
answers = []

for _ in range(T):
    is_break = defaultdict(bool)
    N, C = map(int, input().split())
    memo = [[False for __ in range(N)] for _ in range(N)]
    grid = [input() for _ in range(N)]
    queue = deque([[N - 1, C - 1]])
    memo[N - 1][C - 1] = True
    is_break[C - 1] = True
    while queue:
        r, c = queue.popleft()
        for a, b in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1)]:
            if 0 <= a < N and 0 <= b < N and (not memo[a][b]):
                if grid[a][b] == "#":
                    if b not in is_break:
                        flag = True
                        for i in range(a + 1, N):
                            if grid[i][b] == "#":
                                flag = False
                        is_break[b] = flag
                        if flag:
                            queue.append([a, b])
                            memo[a][b] = True
                    elif is_break[b]:
                        queue.append([a, b])
                        memo[a][b] = True
                else:
                    queue.append([a, b])
                    memo[a][b] = True
    ans = [1 if memo[0][_] else 0 for _ in range(N)]
    print(*ans, sep="")
