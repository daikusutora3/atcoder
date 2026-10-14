N = int(input())
a = list(map(int, input().split()))


ans = 0
while True:
    b = -1
    bi = -1
    for i in range(N):
        if a[i] > b:
            b = max(b, a[i])
            bi = i
    ans += a[bi] // N
    for i in range(N):
        if i == bi:
            continue
        a[i] += a[bi] // N
    a[bi] %= N

    is_ok = True
    for i in range(N):
        if not 0 <= a[i] <= N - 1:
            is_ok = False
    if is_ok:
        break

print(ans)
