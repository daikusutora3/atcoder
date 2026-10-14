T = int(input())

for _ in range(T):
    ans = []
    N = int(input())
    X = list(map(int, input().split()))
    for i in range(1, N + 1):
        if X[i - 1] == 0:
            continue
        ans.append((i, X[i - 1]))
        for k in range(2, N + 1):
            if i * k > N:
                break
            X[i * k - 1] -= X[i - 1]
        X[i - 1] = 0
    print(len(ans))
    for k, x in ans:
        print(k, x)
