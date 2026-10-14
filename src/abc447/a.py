N, M = map(int, input().split())

now = 1
while now <= N:
    M -= 1
    now += 2

# print(M, now)
print("Yes" if M <= 0 else "No")
