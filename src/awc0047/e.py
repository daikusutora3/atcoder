from atcoder.string import z_algorithm

N, Q = map(int, input().split())
S = input()
z = z_algorithm(S) + [0]
rev_S = S[::-1]
rev_z = [0] + z_algorithm(rev_S)[::-1]

# 各i番目を境にしたときのpref, sufの合体したもののが最長になるような(L, R)
z_LR = [(rev_z[i], z[i]) for i in range(len(z))]

# 各Lの値に対して、SSの境界を跨ぐ連続部分文字列のLに対してのRの最大値
saiteki = [-1 for i in range(N + 1)]
for l, r in z_LR:
    saiteki[l] = max(saiteki[l], r)

for i in range(N, 0, -1):
    saiteki[i - 1] = max(saiteki[i - 1], saiteki[i])

# print(z_LR)
# print(saiteki)

for _ in range(Q):
    L, R = map(int, input().split())
    length = R - L + 1
    L, R = (L - 1) % N, (R - 1) % N
    if length > N:
        print("No")
    elif L <= R:
        print("Yes")
    else:
        if R + 1 <= saiteki[N - L]:
            print("Yes")
        else:
            print("No")
