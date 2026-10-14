N = int(input())

ansi = 0
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    if ans < A + B:
        ans = A + B
        ansi = _ + 1

print(ansi)
