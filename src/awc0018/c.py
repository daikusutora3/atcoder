import sys


input = sys.stdin.readline

N, Q = map(int, input().split())
S = [input().strip() for _ in range(N)]

komoji = [chr(i) for i in range(97, 123)]
# key: 元々の文字
# value: 最終的な変換後の文字
d = dict()
for c in komoji:
    d[c] = c


for _ in range(Q):
    a, b = input().split()
    for c in komoji:
        if d[c] == a:
            d[c] = b

for i in range(N):
    ans = ""
    for s in S[i]:
        ans += d[s]
    print(ans)
