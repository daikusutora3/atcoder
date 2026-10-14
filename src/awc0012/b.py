N, T, C, D = map(int, input().split())
W = list(map(int, input().split()))
flag = [1 if W[i] >= T else 0 for i in range(N)]
print(sum(flag) * min(C, D))
