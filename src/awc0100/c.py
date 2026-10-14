N, L, Q = map(int, input().split())

S = [input() for _ in range(N)]

for _ in range(Q):
    ans = ["0" for i in range(L)]
    C = list(map(int, input().split()))[1:]
    for c in C:
        for l in range(L):
            if S[c - 1][l] == "1":
                ans[l] = "1"
    print("".join(ans))
