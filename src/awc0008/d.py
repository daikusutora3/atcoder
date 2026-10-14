N, M = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(M)]
LR.sort()
if M == 0:
    print(N)
    exit()

now = 0
last_r = 0
i = 0
while N > 0:
    # もう雨が降らないとき
    if i >= M:
        now += N
        break
    l, r = LR[i]
    # 最後に雨の降った日 < 次に降り始める日
    if last_r < l:
        # 残りの種を次の雨が降り始めるまでに植え切れる
        if N <= l - last_r - 1:
            now += N
            break
        N -= l - last_r - 1
    last_r = max(last_r, r)
    now = last_r
    i += 1

print(now)
