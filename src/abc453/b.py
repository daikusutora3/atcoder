T, X = map(int, input().split())
A = list(map(int, input().split()))
now = A[0]
print(0, now)

for i in range(1, T + 1):
    if abs(now - A[i]) >= X:
        now = A[i]
        print(i, now)
