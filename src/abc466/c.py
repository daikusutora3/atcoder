N = int(input())

r = 0
ans = 0
for l in range(1, N):
    if r <= l:
        r = l + 1
    while r < N + 1:
        print(f"? {l} {r}")
        res = input()
        if res == "Yes":
            r += 1
        else:
            break
    ans += r - l - 1

print("!", ans)
