from bisect import bisect_left

N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))
C = min(C)

rui = [0 for i in range(N + 1)]
for i in range(N):
    rui[i + 1] += rui[i] + W[i]

# print(C, rui)
ans = 0
for l in range(N):
    r = bisect_left(rui, C + rui[l] + 1)
    # print(C + rui[l])
    # print(f"{l}~{r}")
    ans += r - l - 1

print(ans)
