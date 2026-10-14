from collections import defaultdict

T = int(input())
answers = []


def solve():
    ans = 0
    N = int(input())
    R = list(map(int, input().split()))
    d = defaultdict(set)
    for i in range(N):
        d[R[i]].add(i)
    for _ in range(N):
        sita = _ + 1
        for i in d[_]:
            # 左側を更新
            l = i - 1
            if 0 <= l and 1 < R[l] - R[i]:
                ans += R[l] - R[i] - 1
                d[R[l]].remove(l)
                d[sita].add(l)
                R[l] = sita
            # 右側を更新
            r = i + 1
            if r < N and 1 < R[r] - R[i]:
                ans += R[r] - R[i] - 1
                d[R[r]].remove(r)
                d[sita].add(r)
                R[r] = sita
    return ans


for _ in range(T):
    answers.append(solve())

print(*answers, sep="\n")
