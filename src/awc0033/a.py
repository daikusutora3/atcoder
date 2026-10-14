N, K = map(int, input().split())
S = input()
T = input()

cnt = 0
for i in range(N):
    if S[i] != T[i]:
        cnt += 1

print(max(0, cnt - K))
