N = int(input())

pp = 0
dp = 0

for _ in range(N):
    A, B = map(int, input().split())
    pp += A
    dp += B

print(min(pp, dp))
