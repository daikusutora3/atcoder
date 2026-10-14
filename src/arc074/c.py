H, W = map(int, input().split())


ans = float("inf")

if H % 3 == 0 or W % 3 == 0:
    ans = 0
else:
    ans = min(H, W)

s1 = 0
s2 = 0
s3 = 0

for h1 in range(max(0, H // 3 - 10), min(H // 3 + 10, H)):
    s1 = h1 * W
    for w2 in range(max(0, W // 2 - 10), min(W // 2 + 10, W)):
        s2 = w2 * (H - h1)
        s3 = (W - w2) * (H - h1)
        ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))

H, W = W, H

s1 = 0
s2 = 0
s3 = 0

for h1 in range(max(0, H // 3 - 10), min(H // 3 + 10, H)):
    s1 = h1 * W
    for w2 in range(max(0, W // 2 - 10), min(W // 2 + 10, W)):
        s2 = w2 * (H - h1)
        s3 = (W - w2) * (H - h1)
        ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))

print(ans)
