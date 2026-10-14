N = int(input())
X = list(map(int, input().split()))

if max(X) < 0:
    print("Yes")
else:
    print("No")
