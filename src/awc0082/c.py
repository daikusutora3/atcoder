R, B = map(int, input().split())
T = input()

if not (T.count("R") == R and T.count("B") == B):
    print(-1)
    exit()

cnt = 0
i = 0
while i < R + B:
    while i + 1 < R + B and T[i] == T[i + 1]:
        i += 1
    if T[i] == "B":
        cnt += 1
    i += 1

if T[-1] == "B":
    cnt -= 1

print(cnt)
