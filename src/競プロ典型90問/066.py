N = int(input())

kitai = [0 for i in range(100)]
ans = 0
for _ in range(N):
    L, R = map(int, input().split())
    length = R - L + 1
    for a_i in range(L - 1, R):
        ans += sum(kitai[a_i + 1 :]) / length
    for a_i in range(L - 1, R):
        kitai[a_i] += 1 / length

print(ans)
