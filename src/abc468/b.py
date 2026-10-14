M, D = map(int, input().split())

ans = [1 for i in range(M)]

S = input()

for i, s in enumerate(S):
    if s == "G":
        for j in range(max(0, i - D), min(M, i + D + 1)):
            ans[j] = 0


print(sum(ans))
