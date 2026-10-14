T = int(input())

for _ in range(T):
    N, A, B = map(int, input().split())
    if (N % 2 == 1) or (N % 2 == 0 and (A + B) % 2 == 0):
        print("No")
    else:
        # 右左の移動
        i, j = 0, 0
        # 0: 右, 1: 左, 2: ぶつかったとき
        flag = 0
        for i in range(N * N - 2):
            ni, nj = i, j
            if flag == 0:
                # まだ右に行けるとき
                if j + 1 < N:
                    nj += 1
                # もう右に行けないとき
                else:
                    ni += 1
            elif flag == 1:
                # まだ左に行けるとき
                if j - 1 >= 0:
                    nj -= 1
                # もう左に行けないとき
                else:
                    ni += 1
            if ni == A - 1 and nj == B - 1:
                pass
