N = int(input())

S = list(input().split())

ans = []
for s in S:
    if s[0] in {"a", "b", "c"}:
        ans.append("2")
    if s[0] in {"d", "e", "f"}:
        ans.append("3")
    if s[0] in {"g", "h", "i"}:
        ans.append("4")
    if s[0] in {"j", "k", "l"}:
        ans.append("5")
    if s[0] in {"m", "n", "o"}:
        ans.append("6")
    if s[0] in {"p", "q", "r", "s"}:
        ans.append("7")
    if s[0] in {"t", "u", "v"}:
        ans.append("8")
    if s[0] in {"w", "x", "y", "z"}:
        ans.append("9")

print("".join(ans))
