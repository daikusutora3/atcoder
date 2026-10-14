N, K, M = map(int, input().split())
S = list(map(int, input().split()))
LRP = [list(map(int, input().split())) for i in range(M)]


ans = 0
for bit in range(2**N):
    if bit.bit_count() > K:
        continue
    beauty = 0
    for i in range(N):
        if bit >> i & 1:
            beauty += S[i]
    contest = 0
    for j in range(M):
        is_join = False
        L, R, P = LRP[j]
        for k in range(L - 1, R):
            if bit >> k & 1:
                is_join = True
        if is_join:
            contest += P
    ans = max(ans, beauty + contest)

print(ans)
