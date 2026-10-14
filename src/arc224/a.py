def solve():
    K = int(input())
    ans = 0
    for a in range(1, 101):
        s = str(K * a)
        flag = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1] and s[i] == "0":
                flag = True
                ans = int(s)
                break
        if flag:
            break
    print(ans)


T = int(input())
for _ in range(T):
    solve()
