# linked_list

## Summary

- `0, 1, ..., n - 1` の整数をノード ID として、順序を双方向連結リストで管理する
- 各 ID はリスト内に高々 1 回だけ登場できる
- `prev` / `next` を配列で持つため、既知の ID の削除・挿入・先頭や末尾への移動は `O(1)`
- 値による探索や添字によるランダムアクセスは提供しない

## Functions

| Function | Description | Complexity |
| --- | --- | --- |
| `IndexLinkedList(n, order=None)` | ID の範囲を `0..n-1` とし、`order` の順に初期化する。省略時は `range(n)` | `O(n + K)` |
| `append(x)` / `appendleft(x)` | リスト外の `x` を末尾 / 先頭へ追加する | `O(1)` |
| `insert_after(pos, x)` / `insert_before(pos, x)` | リスト外の `x` を、リスト内の `pos` の直後 / 直前へ追加する | `O(1)` |
| `remove(x)` | リスト内の `x` を外す | `O(1)` |
| `move_to_back(x)` / `move_to_front(x)` | リスト内の `x` を末尾 / 先頭へ移動する | `O(1)` |
| `to_list()` | 現在の順序を Python の `list` にする | `O(K)` |

- `K` は現在リストに含まれるノード数。
- 空のリストを作る場合は `IndexLinkedList(n, [])` とする。
- 範囲外の ID は `IndexError`、挿入済み ID の再挿入や未挿入 ID の削除は `ValueError` になる。
- 使用メモリは `O(n)`。

## Usage

### ABC474 C - Remove and Append

```python
from library.data_structure.linked_list import IndexLinkedList

N, Q = map(int, input().split())
P = [x - 1 for x in map(int, input().split())]

linked = IndexLinkedList(N, P)
for _ in range(Q):
    a = int(input()) - 1
    linked.move_to_back(a)

print(*(x + 1 for x in linked))
```

### 削除したノードを別の位置へ戻す

```python
linked = IndexLinkedList(5, [2, 0, 4])
linked.remove(0)
linked.insert_before(4, 0)
linked.appendleft(1)

print(linked.to_list())  # [1, 2, 0, 4]
```

## References

- [C++ Working Draft N4971 - list modifiers](https://isocpp.org/files/papers/N4971.pdf)
  - 双方向リストでは、位置が既知の単一要素の削除を定数時間で行う設計を確認した
- [collections.deque - Python documentation](https://docs.python.org/3/library/collections.html#collections.deque)
  - `deque` は両端の追加・削除は `O(1)` だが、中央の添字アクセスは `O(n)` になるため、既知 ID へ直接アクセスする配列リンクを採用した

## Related

- 問題: [ABC474 C - Remove and Append](https://atcoder.jp/contests/abc474/tasks/abc474_c)
- 自分の解答: [../../src/abc474/c.py](../../src/abc474/c.py)
