N = int(input())
ans = -1
S = input()
for i in range(N):
    if S[i] == "D":
        ans = i + 1

print(ans)
