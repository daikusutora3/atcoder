T = int(input())

answer = []
for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    ans = float("inf")
    cost_sum = 0
    x = 1
    for i in range(N):
        if (i + 1 + x) % (2 * W) < W:
            cost_sum += C[i]
    x += 1
    ans = min(ans, cost_sum)
    while x <= 2 * W:
        diff_minus = 0
        for i in range((W - 1 - x) % (2 * W), N, 2 * W):
            diff_minus += C[i]
        diff_plus = 0
        for i in range((2 * W - 1 - x) % (2 * W), N, 2 * W):
            diff_plus += C[i]
        cost_sum = cost_sum - diff_minus + diff_plus
        ans = min(ans, cost_sum)
        x += 1
    answer.append(ans)

print(*answer, sep="\n")
