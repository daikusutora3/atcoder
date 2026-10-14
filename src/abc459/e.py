import sys

sys.setrecursionlimit(10**6)

mod = 998244353


# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
def modinv(x):
    global mod
    return pow(x, mod - 2, mod)


modinv_table = [-1] * (10**6 + 1)
for i in range(1, 10**6 + 1):
    modinv_table[i] = modinv(i)


def comb(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

tree = [[] for i in range(N)]
for i, p in enumerate(P):
    v = i + 1
    tree[p - 1].append(v)

flag = False


# [組合せの数, 部分木に残っている飴の数]をreturnする
def dfs(v):
    global flag
    # 葉の時
    if len(tree[v]) == 0:
        if C[v] - D[v] < 0:
            flag = True
        return (comb(C[v], D[v]), C[v] - D[v])
    kumi, ame = 1, 0
    for u in tree[v]:
        ckumi, came = dfs(u)
        kumi = (kumi * ckumi) % mod
        ame += came
    if C[v] + ame - D[v] < 0:
        flag = True
    return ((comb(C[v] + ame, D[v]) * kumi) % mod, C[v] + ame - D[v])


ans = dfs(0)[0]
if flag:
    print(0)
else:
    print(ans)
