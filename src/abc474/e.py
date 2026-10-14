from collections import deque

INF = float("inf")


def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: (x[0] - x[1], x[0]))
    AB = deque(AB)
    min_A = float("inf")
    for i in range(N):
        min_A = min(min_A, AB[i][0])
    ans = 0
    while len(AB) > 1:
        A1, B1 = AB.popleft()
        _, B2 = AB.pop()
        if A1 + B2 > min_A * 2 + B1 + B2:
            ans += min_A * 2 + B1 + B2
        else:
            ans += A1 + B2
    if len(AB):
        A, B = AB.pop()
        ans += min(A, B + min_A)
    print(ans)


T = int(input())
for _ in range(T):
    solve()
