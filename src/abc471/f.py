import sys
from functools import cmp_to_key

N, K = map(int, input().split())


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


S = [input() for i in range(N)]
S.sort(key=lambda x: (len(x), INT(x)), reverse=True)


S1 = S[:K]


def cmp(x, y):
    a = x + y
    b = y + x
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0


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

ans = [ans1, ans2]
ans.sort(lambda x: (len(x), x))

print(ans[-1])
