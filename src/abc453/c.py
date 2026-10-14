N = int(input())
L = list(map(int, input().split()))

ans = 0
for bit in range(2**N):
    cnt = 0
    now = 0.5
    for i in range(N):
        if bit >> i & 1:
            if now < 0 and now + L[i] > 0:
                cnt += 1
            now += L[i]
        else:
            if now > 0 and now - L[i] < 0:
                cnt += 1
            now -= L[i]
    ans = max(ans, cnt)

print(ans)
