N = int(input())
A = list(map(int, input().split()))

cnt1 = 0
cnt10 = 0
cnt100 = 0

for i in range(N):
    oturi = (1000 - A[i] % 1000) % 1000
    cnt1 += oturi % 10
    cnt10 += (oturi % 100) // 10
    cnt100 += (oturi % 1000) // 100

print(cnt1, cnt10, cnt100)
