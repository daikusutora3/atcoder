N, S, L = map(int, input().split())
A = list(map(int, input().split()))
B = [0]

for i in range(N - 1):
    B += [B[-1] + A[i]]

ans = 1
for a in range(S):
    for b in range(max(1, N - S + 1)):
        left = B[S - 1] - B[S - a - 1]
        right = B[S + b - 1] - B[S - 1]
        if right < left:
            left, right = right, left
        if left * 2 + right <= L:
            ans = max(ans, b + a + 1)

print(ans)
