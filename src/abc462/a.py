S = input()
ans = []
for s in S:
    if "0" <= s <= "9":
        ans.append(s)

print("".join(ans))
