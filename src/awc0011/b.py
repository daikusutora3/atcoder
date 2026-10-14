H, W, K = map(int, input().split())
c_1, c_2 = input().split()
grid = [input().replace("#", c_1).replace(".", c_2) for _ in range(H)]

for i in range(H * K):
    ans = []
    for j in range(W * K):
        ans.append(grid[i // K][j // K])
    print("".join(ans))
