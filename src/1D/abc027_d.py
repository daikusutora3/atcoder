S = input()

N = len(S)
cnt_plus = [0 for i in range(N + 1)]
cnt_minus = [0 for i in range(N + 1)]


for i in range(N - 1, -1, -1):
    cnt_plus[i] += cnt_plus[i + 1] + (1 if S[i] == "+" else 0)
    cnt_minus[i] += cnt_minus[i + 1] + (1 if S[i] == "-" else 0)


res = []
m_cnt = 0
for i in range(N):
    if S[i] == "M":
        m_cnt += 1
        res.append((cnt_plus[i] - cnt_minus[i], i))

res.sort(reverse=True)

migi = {i for d, i in res[: m_cnt // 2]}
ans = 0
now = 0
for i in range(N):
    if S[i] == "M":
        if i in migi:
            now += 1
        else:
            now -= 1
    elif S[i] == "+":
        ans += now
    else:
        ans -= now

print(ans)
