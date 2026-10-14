N, K, M = map(int, input().split())
D = []

for _ in range(K):
    b, d = map(int, input().split())
    D.append(d)

D.sort(reverse=True)
print(sum(D[::M]) * 2)
