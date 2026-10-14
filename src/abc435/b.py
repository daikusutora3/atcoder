import itertools

N = int(input())
A = list(map(int, input().split()))
ind = [i for i in range(N)]
ans = 0
for l, r in itertools.combinations_with_replacement(ind, 2):
    sum = 0
    for i in range(l, r + 1):
        sum += A[i]
    flag = True
    for i in range(l, r + 1):
        if sum % A[i] == 0:
            flag = False
    # print((l + 1, r + 1), sum, A[l : r + 1], flag)
    if flag:
        ans += 1

print(ans)
