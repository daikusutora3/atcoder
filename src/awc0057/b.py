N = int(input())
S = [list(input().split())[1:] for i in range(N)]
Q = int(input())


def bubun(S, T):
    now = 0
    for t in T:
        while now < len(S) and S[now] != t:
            now += 1
        if now == len(S):
            return False
        now += 1
    return True


for _ in range(Q):
    T = input()
    ans = 0
    for SS in S:
        check = False
        for s in SS:
            if bubun(s, T):
                check = True
        if check:
            ans += 1
    print(ans)
