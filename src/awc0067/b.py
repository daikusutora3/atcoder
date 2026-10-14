N = int(input())

B = list(map(int, input().split()))
ans = -float("inf")
end_here = 0

for i in range(N):
    end_here = max(B[i], B[i] + end_here)
    ans = max(ans, end_here)
    print(ans)
