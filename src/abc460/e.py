# ある値 a < x <= bのmod mがcであるものの個数
def f(a, b, c, m):
    # print(f"{a} < x <= {b}: mod {m}が{c}であるものの個数")
    # res = []
    # for i in range(a + 1, b + 1):
    #     if i % m == c:
    #         res.append(i)
    # print(len(res))
    # print(res)
    return (b - c) // m - (a - c) // m


def solve(N, M):
    for k in range(19):
        pass
