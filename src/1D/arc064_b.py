import sys

S = input()

flag = True
for i in range(2, len(S), 2):
    if S[i] != S[i - 2]:
        flag = False
for i in range(3, len(S), 2):
    if S[i] != S[i - 2]:
        flag = False
# ababababaのとき
if flag:
    print("Second")
    sys.exit()

moji = {s for s in S}
if len(moji) == 3:
    a, b, c = moji
    l = [(S.count(a), a), (S.count(b), b), (S.count(c), c)]
    l.sort()
    if l[0][0] == 1:
        ind = S.index(l[0][1])
        if 0 < ind < len(S):
            T = S[:ind] + S[ind + 1 :]
            flag = True
            for i in range(2, len(S), 2):
                if S[i] != S[i - 2]:
                    flag = False
            for i in range(3, len(S), 2):
                if S[i] != S[i - 2]:
                    flag = False
            if flag:
                print("First")
                sys.exit()

if len(S) % 2 == 0:
    if S[0] == S[-1]:
        print("First")
    else:
        print("Second")
else:
    if S[0] == S[-1]:
        print("Second")
    else:
        print("First")
