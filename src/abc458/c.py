S = input()

ans = 0
for i, s in enumerate(S):
    if s == "C":
        ans += min(i + 1, len(S) - i)
print(ans)
