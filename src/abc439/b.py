N = int(input())

s = set()
ans = False
while True:
    new = 0
    for n in str(N):
        new += int(n) * int(n)
    if new in s:
        break
    s.add(N)
    if new == 1:
        ans = True
        break
    N = new

print("Yes" if ans else "No")
