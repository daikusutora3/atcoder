N, K = map(int, input().split())
FB = [list(map(int, input().split())) for i in range(N)]

ans = 0
for bit in range(2**N):
    res = 0
    if bit.bit_count() != K:
        continue
    for i in range(N):
        if bit >> i & 1:
            res += FB[i][1]
        else:
            res += FB[i][0]
    ans = max(ans, res)

print(ans)
