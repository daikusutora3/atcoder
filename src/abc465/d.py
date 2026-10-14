def solve():
    X, Y, K = map(int, input().split())
    if X == Y:
        print(0)
        return
    # (l, r)のtupple
    que = []
    ans = 0
    while True:
        ans += 1
        for i, (l, r) in enumerate(que):
            que[i] = (min(l * K, 10**18 + 10), min(((r + 1) * K) - 1, 10**18 + 10))
        que.append((X * K, ((X + 1) * K) - 1))
        X = X // K
        flag = False
        if X == Y:
            flag = True
        for l, r in que:
            if l <= Y <= r:
                flag = True
        if flag:
            break
    print(ans)


T = int(input())
for _ in range(T):
    solve()
