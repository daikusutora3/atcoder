N = int(input())
ans = [str(i + 1) for i in range(N - 1, -1, -1)]

print(",".join(ans))
