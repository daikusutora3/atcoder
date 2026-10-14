import sys

input = sys.stdin.readline

# ローリングハッシュの設定
BASE = 3
MOD = 699999953  # 競プロでよく使われる大きめの素数


def to_num(c: str) -> int:
    """'R', 'G', 'B' を 0, 1, 2 に変換する"""
    if c == "R":
        return 0
    if c == "G":
        return 1
    return 2


def count_for_one_color(S, T, target_color):
    """
    target_color (0,1,2) を固定して、
    「その色で単色になる対角線」が何本あるかを数える。

    S, T は 0/1/2 の整数列。
    """
    n = len(S)

    # need[j] = target_color - T[j] (mod 3)
    # 対角線が全部 target_color になるためには、
    # 対応する位置で S[i] == need[j] になればよい。
    need = [(target_color - t) % 3 for t in T]

    ans = 0

    # ------------------------------------------------------------
    # 1. S の prefix と need の suffix を比較する
    #
    # 長さ L = 1..N について
    #   S[0:L] == need[N-L:N]
    # なら、ある対角線が target_color で単色になる。
    # ------------------------------------------------------------
    hash_s = 0
    hash_need = 0
    pow_base = 1  # BASE^(L-1)

    for L in range(1, n + 1):
        # S 側: 末尾に 1 文字足していく
        # 例: [a,b,c] -> ((a)*B + b)*B + c
        hash_s = (hash_s * BASE + S[L - 1]) % MOD

        # need 側: suffix を「左から読んだ形」と同じハッシュになるように作る
        # need[N-L] が先頭文字、need[N-1] が末尾文字になる
        hash_need = (hash_need + need[n - L] * pow_base) % MOD

        if hash_s == hash_need:
            ans += 1

        pow_base = (pow_base * BASE) % MOD

    # ------------------------------------------------------------
    # 2. S の suffix と need の prefix を比較する
    #
    # 長さ L = 1..N-1 について
    #   S[N-L:N] == need[0:L]
    # なら、別の向きの対角線が target_color で単色になる。
    #
    # L=N は 1. ですでに数えているので、ここでは N-1 まで。
    # ------------------------------------------------------------
    hash_s = 0
    hash_need = 0
    pow_base = 1  # BASE^(L-1)

    for L in range(1, n):
        # S の suffix を左から読んだ文字列のハッシュになるように作る
        # S[N-L] が先頭文字
        hash_s = (hash_s + S[n - L] * pow_base) % MOD

        # need 側は prefix を普通に右へ伸ばす
        hash_need = (hash_need * BASE + need[L - 1]) % MOD

        if hash_s == hash_need:
            ans += 1

        pow_base = (pow_base * BASE) % MOD

    return ans


def main():
    N = int(input())
    S = [to_num(c) for c in input().strip()]
    T = [to_num(c) for c in input().strip()]

    ans = 0

    # 単色の色を 0,1,2 (= R,G,B) で全探索
    for color in range(3):
        ans += count_for_one_color(S, T, color)

    print(ans)


if __name__ == "__main__":
    main()
