def unpack(S):
    i = 0
    s = set()
    for i in range(len(S) - 2):
        if S[i : i + 2] == "xx":
            l = i - 1
            r = i + 2
            while 0 <= l and r < len(S) and S[l] == "(" and S[r] == ")":
                s.add(l)
                s.add(r)
                l -= 1
                r += 1
    res = []
    for i in range(len(S)):
        if i not in s:
            res.append(S[i])
    return "".join(res)


# print("x(xx)", "->", unpack("x(xx)"))
# print("(((((xx)))))x", "->", unpack("(((((xx)))))x"))


T = int(input())

for _ in range(T):
    A = input()
    B = input()
    if unpack(A) == unpack(B):
        print("Yes")
    else:
        print("No")
