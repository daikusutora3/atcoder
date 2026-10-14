N, M = map(int, input().split())

top = float("inf")
bottom = -float("inf")
right = -float("inf")
left = float("inf")

for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == "#":
            top = min(top, i)
            left = min(left, j)
            right = max(right, j)
            bottom = max(bottom, i)


print((bottom - top + 1) * (right - left + 1))
