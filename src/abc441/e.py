from sortedcontainers import SortedList

N = int(input())
S = input()

imos_data = {"A": 1, "B": -1, "C": 0}
imos = [imos_data[s] for s in S]

for i in range(N - 1):
    imos[i + 1] += imos[i]

sl = SortedList([0])

ans = 0
for i in range(N):
    br = sl.bisect_right(imos[i] - 1)
    ans += br
    sl.add(imos[i])

print(ans)
