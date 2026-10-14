from sortedcontainers import SortedList


N = int(input())
a = list(map(int, input().split()))


ans = -float("inf")

slp = SortedList(a[:N])
slm = SortedList(a[N:])
# print(slp, slm)
now = sum(slp) - sum(slm[:N])
ans = max(ans, now)
# print(sum(slp[-N:]) - sum(slm[:N]), now)

for i in range(N):
    move = a[N + i]
    # print(f"==={move}===")
    # minus -> plusに移動する
    if slm.bisect_left(move) < N:
        now += move - slm[N]
    slm.discard(move)
    slp.add(move)
    if not (slp.bisect_left(move) <= i):
        now += move - slp[i]
    ans = max(ans, now)

print(ans)
