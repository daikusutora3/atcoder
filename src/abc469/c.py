N = int(input())
S = input()


ans = [-1 for i in range(N)]
cnt = 0
for i in range(N):
    if S[i] == "x":
        ans[cnt] = i + 1
        cnt += 1

for i in range(N):
    if ans[i] == -1:
        ans[i] = len(ans)

print(*ans)
