N, M = map(int, input().split())
W = list(map(int, input().split())) if N != 1 else []
ans = 1
for i in range(N - 1):
    if W[i] == 1:
        if M > 0:
            M -= 1
        else:
            break
    ans = i + 2

print(ans)
