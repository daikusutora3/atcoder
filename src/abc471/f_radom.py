from functools import cmp_to_key
from itertools import combinations
from random import randint


def del_pref_0(s):
    pref_0cnt = 0
    for i in range(len(s)):
        if int(s[i]) == 0:
            pref_0cnt += 1
        else:
            break
    if len(s) == pref_0cnt:
        return "0"
    else:
        return s[pref_0cnt:]


def INT(s):
    return int(del_pref_0(s))


def cmp(x, y):
    a = x + y
    b = y + x
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0


def solve(N, K, S):
    S.sort(key=lambda x: (len(x), INT(x)), reverse=True)
    S1 = S[:K]
    S1.sort(key=cmp_to_key(cmp))
    ans1 = del_pref_0("".join(S1))
    S2 = S[: K - 1]
    m = -1
    mi = -1
    for i in range(K - 1, N):
        if m < INT(S[i]):
            m = INT(S[i])
            mi = i
    S2.append(S[mi])
    S2.sort(key=cmp_to_key(cmp))
    ans2 = del_pref_0("".join(S2))
    if int(ans1) > int(ans2):
        return ans1
    else:
        return ans2


def naive(N, K, S):
    ans = "0"
    for com in combinations(S, K):
        com = list(com)
        com.sort(key=cmp_to_key(cmp))
        res = del_pref_0("".join(com))
        if int(ans) < int(res):
            ans = res
    return ans


def main():
    N = randint(1, 5)
    K = randint(1, N)
    S = []
    for i in range(N):
        x = ""
        keta = randint(1, 4)
        for _ in range(keta):
            x += str(randint(0, 9))
        S.append(x)
    if naive(N, K, S[:]) != solve(N, K, S[:]):
        print(f"{(N, K, S[:])}: {naive(N, K, S[:])}, {solve(N, K, S[:])}")


for i in range(1000):
    main()


# print(naive(3, 2, ["123", "45", "6"]))
