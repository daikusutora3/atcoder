N, W = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

ans = 0
for bit in range(2**N):
    asum = 0
    bsum = 0
    for i in range(N):
        if bit >> i & 1:
            A, B = AB[i]
            asum += A
            bsum += B
    if bsum <= W:
        ans = max(ans, asum)

print(ans)
