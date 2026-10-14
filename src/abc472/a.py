S = input()
ans = []

for s in S:
    if s == "A":
        ans.append(s)
    else:
        ans.append(".")

print("".join(ans))
