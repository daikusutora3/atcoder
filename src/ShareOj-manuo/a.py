N, W, P = map(int, input().split())
T = list(map(int, input().split()))
t_min = sum(T)

if t_min < W:
    print("WR")
elif t_min < P:
    print("PB")
else:
    print("Reset")
