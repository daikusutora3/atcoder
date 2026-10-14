N = int(input())

MR = 0
ans = 0
for i in range(N):
    T, R = map(int, input().split())
    ans += T + R
    MR = max(MR, R)

print(ans - MR)
