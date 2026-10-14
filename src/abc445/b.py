N = int(input())
S = [input() for _ in range(N)]
m = max(len(S[i]) for i in range(N))

ans = [
    "." * ((m - len(S[i])) // 2) + S[i] + "." * ((m - len(S[i])) // 2) for i in range(N)
]
print(*ans, sep="\n")
