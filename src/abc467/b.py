N = int(input())
X = 10000
Y = 10000

for _ in range(N):
    A, B, S = input().split()
    A = int(A)
    B = int(B)
    if S == "keep":
        X -= B
    else:
        X -= A
    Y -= A

print(Y - X)
