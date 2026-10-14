import sys

K = int(input())

for N in range(2, 51):
    k = K
    # 0, 1, 2... N−１の長さNの配列から逆操作をすることを考える
    A = [i + k // N for i in range(N)]
    for i in range(k % N):
        A[i] += N
        for j in range(N):
            if j == i:
                continue
            A[j] -= 1
    check = True
    for a in A:
        if not 0 <= a <= 10**16 + 1000:
            check = False
    if check:
        print(N)
        print(*A)
        sys.exit()
