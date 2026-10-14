X = int(input())

ans = []
# 後ろにあるCの個数
now = 25
for i in range(50):
    if X >= now:
        ans.append("A")
        ans.append("R")
        X -= now
    else:
        ans.append("C")
        ans.append("R")
        now -= 1

ans = "".join(ans[:-1])

print(ans)
