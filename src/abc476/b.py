N = int(input())

S = input()
T = input()

ans = True

for i in range(N):
    if S[i] == "*" or T[i] == "*":
        pass
    elif S[i] == T[i]:
        pass
    else:
        ans = False

print("Yes" if ans else "No")
