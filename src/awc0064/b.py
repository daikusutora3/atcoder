N = int(input())

A = list(map(int, input().split()))
A.sort(key=lambda x: -x)

tak = 0
aok = 0
for i in range(N):
    if i % 2 == 0:
        tak += A[i]
    else:
        aok += A[i]

print(tak - aok)
