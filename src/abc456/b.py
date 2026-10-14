A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

U = 6 * 6 * 6
cnt = 0

for i in range(6):
    for j in range(6):
        for k in range(6):
            if set({A1[i], A2[j], A3[k]}) == {4, 5, 6}:
                cnt += 1

print(cnt / U)
