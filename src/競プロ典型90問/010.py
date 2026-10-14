N = int(input())

r_1 = [0 for i in range(N + 1)]
r_2 = [0 for i in range(N + 1)]

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        r_1[i + 1] += p
    else:
        r_2[i + 1] += p
    r_1[i + 1] += r_1[i]
    r_2[i + 1] += r_2[i]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(r_1[r] - r_1[l - 1], r_2[r] - r_2[l - 1])
