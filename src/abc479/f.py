from sortedcontainers import SortedList

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
Si = [[S[i], i] for i in range(N)]
Si.sort()
diff = [0 for i in range(N)]
swap_cnt = 0
sl = SortedList()
for i in range(N):
    j = Si[i][1]
    diff[j] -= len(sl) - sl.bisect_left(T[j])
    swap_cnt += len(sl) - sl.bisect_left(T[j])
    # print(f"{j + 1}の人はより左にいる{len(sl) - sl.bisect_left(T[j])}人の人とswapする")
    sl.add(T[j])

sl = SortedList()
for i in range(N - 1, -1, -1):
    j = Si[i][1]
    diff[j] += sl.bisect_left(T[j])
    # print(f"{j + 1}の人はより右にいる{sl.bisect_left(T[j])}人の人とswapする")
    sl.add(T[j])

ans = 0
for i in range(N):
    ans += abs(S[i] - T[i] + diff[i])

print(ans + swap_cnt)
