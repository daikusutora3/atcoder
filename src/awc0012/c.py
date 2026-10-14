N, K, M = map(int, input().split())

keiken = []
no_keiken = []

for i in range(N):
    h, p = map(int, input().split())
    if h == 1:
        keiken.append(p)
    else:
        no_keiken.append(p)


keiken.sort(reverse=True)
no_keiken.sort(reverse=True)

if len(keiken) < M or len(no_keiken) < K - M:
    print(-1)
else:
    print(sum(keiken[:M]) + sum(no_keiken[: K - M]))
