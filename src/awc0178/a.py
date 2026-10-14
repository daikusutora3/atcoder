N = int(input())

ans = []
for _ in range(N):
    A, B = map(int, input().split())
    if A < B:
        ans.append("L")
    elif A == B:
        ans.append("E")
    else:
        ans.append("H")

print("".join(ans))
