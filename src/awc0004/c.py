N = int(input())
H = list(map(int, input().split()))

H.sort()

ans = 0
tmp = 0
for i in range(N):
    ans += abs(tmp - H[i])
    tmp = H[i]

print(ans + abs(tmp))