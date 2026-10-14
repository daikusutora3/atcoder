N, M, K = map(int, input().split())
uwasa = {i + 1 for i in range(K)}
for _ in range(M):
    a, b = map(int, input().split())
    if a in uwasa or b in uwasa:
        uwasa.add(a)
        uwasa.add(b)

print(len(uwasa))
