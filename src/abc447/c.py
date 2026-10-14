S = input()
T = input()

S += "#"
T += "#"
i = 0
j = 0
ans = 0
flag = True
while i < len(S) and j < len(T):
    if S[i] == T[j]:
        i += 1
        j += 1
    elif S[i] == "A":
        ans += 1
        i += 1
    elif T[j] == "A":
        ans += 1
        j += 1
    else:
        flag = False
        break

print(ans if flag else -1)
