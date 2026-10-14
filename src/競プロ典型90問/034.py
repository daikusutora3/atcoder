from collections import defaultdict, deque


N, K = map(int, input().split())
A = list(map(int, input().split()))
l, r = 0, 0
d = defaultdict(deque)
s = set()

ans = 0
while l < N:
    # ある要素A[r]を新たに追加するとき
    if len(s) <= K and r < N:
        s.add(A[r])
        d[A[r]].append(r)
        r += 1
        if len(s) <= K:
            ans = max(ans, r - l)
    # ある要素A[l]を削除するとき
    else:
        d[A[l]].popleft()
        if len(d[A[l]]) == 0:
            s.remove(A[l])
        l += 1

print(ans)
