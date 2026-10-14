N = int(input())
S = input()
T = input()


ans = []
for i in range(N):
    if S[i] == T[i]:
        ans.append(S[i])
    elif S[i] == "?" and T[i] == "?":
        ans.append("?")
    elif S[i] == "?":
        ans.append(T[i])
    elif T[i] == "?":
        ans.append(S[i])
    else:
        ans.append("!")

ans = "".join(ans)
print(ans)
print("Yes" if "!" in ans else "No")
