N, K = map(int, input().split())
W = list(input().split())

rui = [0 for i in range(N + 1)]

for i in range(N):
    if W[i] == "S":
        rui[i + 1] += 1
    rui[i + 1] += rui[i]

# print(rui)
ans = 0
for i in range(N - K + 1):
    # print(rui[i + K] - rui[i])

    ans = max(ans, rui[i + K] - rui[i])

print(ans)
