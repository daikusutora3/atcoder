ans = 0
N = int(input())
S = input()

for i in range(N):
    flag = True
    if S[i] == "o":
        flag = False
    if i != 0 and S[i - 1] == "o":
        flag = False
    if i != N - 1 and S[i + 1] == "o":
        flag = False
    if flag:
        ans += 1

print(ans)
