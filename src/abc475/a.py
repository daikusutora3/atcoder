S = input()

ans = ""
for i in range(len(S)):
    ans += S[i] + "o"

print(ans[:-1])
