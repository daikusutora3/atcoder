N, S, C = map(int, input().split())

R = list(map(int, input().split()))


print(max(0, (sum(R) - S) * C))
