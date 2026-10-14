N = int(input())

t = list(map(int, input().split()))
v = list(map(int, input().split()))

# まず全体を2倍(最後に面積を4で割る)
t = [2 * a for a in t]
v = [2 * a for a in v]

min_v = [0]
# 各区間の上限のスピードで初期化
for i in range(N):
    min_v[-1] = min(min_v[-1], v[i])
    min_v += [v[i]] * t[i]

min_v[-1] = 0


for time in range(1, len(min_v)):
    min_v[time] = min(min_v[time], min_v[time - 1] + 1)

for time in range(len(min_v) - 1, 0, -1):
    min_v[time - 1] = min(min_v[time - 1], min_v[time] + 1)

print(sum(min_v) / 4)
