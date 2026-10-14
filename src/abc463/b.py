N, X = input().split()
N = int(N)
ans = False

d = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

for i in range(N):
    S = input()
    if S[d[X]] == "o":
        ans |= True


print("Yes" if ans else "No")
