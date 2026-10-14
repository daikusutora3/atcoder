N, M = map(int, input().split())

uwasa = [0 for i in range(N)]
uwasa[0] = 1

for _ in range(M):
    a, b = map(int, input().split())
    uwasa[b] |= uwasa[a]

print(sum(uwasa))
