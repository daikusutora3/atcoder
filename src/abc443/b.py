N, K = map(int, input().split())

cnt = 0
last = N
while cnt < K:
    cnt += last
    last += 1

print(last - N - 1)
