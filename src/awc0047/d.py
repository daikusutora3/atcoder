N = int(input())
A = list(map(int, input().split()))
if sum(A) % N != 0:
    print(-1)
    exit()

K = sum(A) // N

ans = 0
pos = 0
for i in range(N):
    while A[i] < K:
        if pos < N and A[pos] > K:
            if A[pos] - K > K - A[i]:
                A[pos] -= K - A[i]
                ans += abs(i - pos) * (K - A[i])
                A[i] = K
            else:
                A[i] += A[pos] - K
                ans += abs(i - pos) * (A[pos] - K)
                A[pos] = K
        else:
            pos += 1

print(ans)
