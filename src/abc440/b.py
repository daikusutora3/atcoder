N = int(input())
T = list(map(int, input().split()))
T_no = [(T[i], i + 1) for i in range(N)]

T_no.sort()

print(T_no[0][1], T_no[1][1], T_no[2][1])
