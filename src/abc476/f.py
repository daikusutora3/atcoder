N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

L = 2 * N - 1
plus = [0 for i in range(L)]
minus = [0 for i in range(L)]
for r in range(N):
    for c in range(N):
        plus[r + c] += A[r] * B[c] % M
        minus[r - c + N - 1] += A[r] * B[c] % M

dplus = [0 for i in range(L)]

for i in range(L):
    dplus[0] += plus[i] * i

left = 0
plus_sum = sum(plus)
for i in range(1, L):
    left += plus[i - 1]
    right = plus_sum - left
    dplus[i] = dplus[i - 1] + left - right


dminus = [0 for i in range(L)]

for i in range(L):
    dminus[0] += minus[i] * i

left = 0
minus_sum = sum(minus)
for i in range(1, L):
    left += minus[i - 1]
    right = minus_sum - left
    dminus[i] = dminus[i - 1] + left - right

ans = 0
for i in range(N):
    for j in range(N):
        fij = (dplus[i + j] + dminus[i - j + N - 1]) // 2
        ans ^= fij + i * N + j

print(ans)
