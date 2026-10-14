N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

V = [A[0]]
for i in range(N - 1):
    V.append(A[i + 1] - A[i])
V.append(L - A[-1])


def is_ok(k):
    global V, K
    s = 0
    num = 0
    for v in V:
        s += v
        if s >= k and num < K:
            s = 0
            num += 1
    # print(f"{k}: {num} 分割 {s}切れ端")
    return num == K and s >= k


ok, ng = 0, 10**10

while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
