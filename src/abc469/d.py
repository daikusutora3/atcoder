N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]
ABs = [frozenset(ab) for ab in AB]

ans = set()
for a in AB[0]:
    # print(f"===={a}====")
    s = -1
    for i in range(1, M):
        if a not in ABs[i]:
            if s == -1:
                s = ABs[i]
            else:
                s &= ABs[i]
    if s == -1:
        for b in range(1, N + 1):
            if a != b:
                ans.add(frozenset({a, b}))
    else:
        for b in s:
            ans.add(frozenset({a, b}))

print(len(ans))
