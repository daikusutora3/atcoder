N, B = map(int, input().split())
A = list(map(int, input().split()))

print("Yes" if sum(A) <= B else "No")
