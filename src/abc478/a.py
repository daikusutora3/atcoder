N, M = map(int, input().split())
grapes = [0] * N

i = 0

while M > 0:
    M -= 1
    grapes[i] += 1
    i = (1 + i) % N

print(*grapes, sep="\n")
