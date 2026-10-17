N, K, T = map(int, input().split())
A = list(map(int, input().split()))
A.append(T)
A.sort()

ans = 0
# シャワーの止まる時刻
time = 0
for i in range(N + 1):
    if time < A[i]:
        cnt = (A[i] - time + K - 1) // K
        ans += cnt
        time = max(time + cnt * K, A[i] + K)
    else:
        time = max(time, A[i] + K)
    if time >= T:
        break

print(ans)
