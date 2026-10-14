N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = [(a, i + 1) for i, a in enumerate(A)]
A.sort()
# print(A)

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    i = 0
    while i < N:
        if A[i][1] not in B:
            print(A[i][0])
            break
        i += 1
