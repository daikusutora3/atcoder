from bisect import bisect_right


N = int(input())
S = input()


orui = [0 for i in range(N + 1)]
xrui = [0 for i in range(N + 1)]

for i in range(N):
    orui[i + 1] += orui[i] + (1 if S[i] == "o" else 0)
    xrui[i + 1] += xrui[i] + (1 if S[i] == "x" else 0)

ans = 0
for l in range(N):
    br = 0
    if S[l] == "o":
        br = bisect_right(xrui, xrui[l])
    if S[l] == "x":
        br = bisect_right(orui, orui[l])
    ans += N - br + 1

print(ans)
