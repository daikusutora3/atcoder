def compress(values):
    """(comp, vals, idx) を返す。

    comp: values と同じ順序・長さの圧縮後リスト
    vals: values に登場する値を昇順に重複除去したリスト
    idx: 元の値から圧縮後 index への辞書

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/misc/compress.md
    """
    vals = sorted(set(values))
    idx = {x: i for i, x in enumerate(vals)}
    comp = [idx[x] for x in values]
    return comp, vals, idx
