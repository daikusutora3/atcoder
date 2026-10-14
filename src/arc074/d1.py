from heapq import heapify, heappop, heappush


N = int(input())
A = list(map(int, input().split()))

plus = A[:N]
heapify(plus)
now = sum(A[:N])
p_res = [now]
for i in range(N, 2 * N):
    heappush(plus, A[i])
    now += A[i]
    a = heappop(plus)
    now -= a
    p_res.append(now)

minus = [-a for a in A[-N:]]
heapify(minus)
now = sum(A[-N:])
m_res = [now]
for i in range(2 * N - 1, N - 1, -1):
    heappush(minus, -A[i])
    now += A[i]
    a = heappop(minus)
    now += a
    m_res.append(now)
    # print(minus)

# print(p_res)
# print(m_res)

ans = -float("inf")

for i in range(len(p_res)):
    # print(p_res[i], m_res[-i - 1])
    ans = max(ans, p_res[i] - m_res[-i - 1])

print(ans)
