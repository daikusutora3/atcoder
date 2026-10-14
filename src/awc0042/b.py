N, S, T = map(int, input().split())
D = list(map(int, input().split()))
D.sort()

for d in D:
    if d <= S:
        S += d

print("Yes" if S >= T else "No")
