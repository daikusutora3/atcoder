N = int(input())

regist = set()
for i in range(N):
    S = input()
    if S not in regist:
        print(i + 1)
    regist.add(S)
