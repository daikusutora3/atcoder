N = int(input())

cnt = 0

for i in range(N):
    a, b, c, d = input().split()
    b = int(b)
    d = int(d)
    if b < d or b == d and a > c:
        cnt += 1

if cnt == 1:
    print("Saikou no Syunkan")
elif cnt > 1:
    print("WA")
else:
    print("AC")
