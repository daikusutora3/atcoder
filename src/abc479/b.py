N = int(input())
S = input()
ans = 0

cnt = 0
for s in S:
    if s == "R":
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)
