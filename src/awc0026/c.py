N, T, E = map(int, input().split())
P = list(map(int, input().split()))
P.sort()

ans = 0
cnt = 0
for p in P:
    if cnt + p * T <= E:
        cnt += p * T
        ans += 1
    else:
        break

print(ans)
