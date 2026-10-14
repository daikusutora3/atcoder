S = input()
bw = []
cnt = 0
for i in range(len(S)):
    if i > 0 and S[i] != S[i - 1]:
        bw.append(cnt)
        cnt = 0
    cnt += 1

bw.append(cnt)
rui_bw = [0 for i in range(len(bw) + 1)]
for i in range(len(bw)):
    rui_bw[i + 1] += rui_bw[i] + bw[i]

ans = bw[0] if len(bw) == 1 else float("inf")
s = sum(bw)
for i in range(len(bw) - 1):
    ans = min(ans, max(rui_bw[i + 1], s - rui_bw[i + 1]))

print(ans)
