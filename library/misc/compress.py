def compress(values):
    """(comp, vals, idx) を返す。

    comp: values と同じ順序・長さの圧縮後リスト
    vals: values に登場する値を昇順に重複除去したリスト
    idx: 元の値から圧縮後 index への辞書

    計算量: 期待時間 O(N + U log(U + 1))、空間 O(N + U)。N は入力数、U は異なる値数。

    Source: https://github.com/daikusutora3/atcoder
    """
    vals = sorted(set(values))
    idx = {x: i for i, x in enumerate(vals)}
    comp = [idx[x] for x in values]
    return comp, vals, idx
