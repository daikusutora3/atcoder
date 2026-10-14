N, K = map(int, input().split())
A = list(map(int, input().split()))

K_set = set()
A_set = [set() for i in range(N)]

for bit in range(61):
    if K >> bit & 1:
        K_set.add(bit)

for i in range(N):
    for bit in range(61):
        if A[i] >> bit & 1:
            A_set[i].add(bit)

ans_bit = set()
ans = 0
for i in range(N):
    if A_set[i] <= K_set:
        ans += 1
        ans_bit |= A_set[i]

if ans_bit == K_set and ans > 0:
    print(ans)
else:
    print(-1)
