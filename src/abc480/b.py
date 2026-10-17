from collections import defaultdict

N, M = map(int, input().split())
S = [input() for i in range(N)]

d = defaultdict(int)
for i in range(N):
    d[S[i]] = 0

for _ in range(M):
    T = input()
    if T in d:
        d[T] += 1
    else:
        kouho = []
        for i in range(len(T)):
            for j in range(97, 123):
                c = chr(j)
                NT = T[:i] + c + T[i + 1 :]
                if NT in d:
                    kouho.append(NT)
        if len(kouho) == 1:
            d[kouho[0]] += 1

for i in range(N):
    print(d[S[i]])
