from bisect import bisect_left, bisect_right


N = int(input())
A = list(map(int, input().split()))
rui = [0 for i in range(N + 1)]

for i in range(N):
    rui[i + 1] += rui[i] + A[i]

ans = float("inf")
for b in range(1, N - 2):
    left, right = rui[b + 1], rui[N] - rui[b + 1]
    lbl = min(b - 1, bisect_left(rui, left // 2) - 1)
    lbr = min(b - 1, bisect_right(rui, left // 2) - 1)
    rbl = min(N - 2, bisect_left(rui, right // 2 + rui[b + 1]) - 1)
    rbr = min(N - 2, bisect_right(rui, right // 2 + rui[b + 1]) - 1)
    # print(f"a: {lbl}~{lbr}, b: {b}, c: {rbl}~{rbr}")
    for a in range(max(0, lbl - 1), lbr + 1):
        for c in range(max(0, rbl - 1), rbr + 1):
            P = rui[a + 1]
            Q = rui[b + 1] - rui[a + 1]
            R = rui[c + 1] - rui[b + 1]
            S = rui[N] - rui[c + 1]
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))

print(ans)
