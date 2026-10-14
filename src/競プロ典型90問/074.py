N = int(input())
S = input()
now = 0
ans = 0
for i in range(N):
    if S[i] == "a":
        pass
    elif S[i] == "b":
        ans += now + 1
    else:
        ans += 2 * (now + 1)
    now = now * 2 + 1

print(ans)
