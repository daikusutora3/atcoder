ans = 0

S = input()
N = len(S)

# 奇数の時
for c in range(N):
    l = c
    r = c
    ans += 1
    cnt = 0
    while l - 1 >= 0 and r + 1 < N:
        l -= 1
        r += 1
        if S[l] != S[r]:
            cnt += 1

        if cnt <= 1:
            ans += 1
        else:
            break


# 偶数の時
for i in range(N - 1):
    l = i
    r = i + 1
    ans += 1
    cnt = 0 if S[l] == S[r] else 1
    while l - 1 >= 0 and r + 1 < N:
        l -= 1
        r += 1
        if S[l] == S[r]:
            pass
        else:
            cnt += 1
        if cnt <= 1:
            ans += 1
        else:
            break


print(ans)
