N = int(input())
P = list(map(int, input().split()))
flag = True
for i in range(10, 101, 10):
    for p in P[i - 10 : i]:
        if not (i - 10 <= p <= i):
            flag = False

print("Yes" if flag else "No")
