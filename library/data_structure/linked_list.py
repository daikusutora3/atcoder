class IndexLinkedList:
    """0..n-1 の整数をノード ID として扱う双方向連結リスト。

    計算量: 構築時間 O(n + K)、空間 O(n)。K は初期要素数。
    挿入・削除・移動・len は O(1)。反復全体と to_list は O(M)、M は現在の要素数。

    Source: https://github.com/daikusutora3/atcoder
    """

    def __init__(self, n, order=None):
        """計算量: 時間 O(n + K)、空間 O(n)。K は order の要素数（省略時 n）。"""
        self.prev = [-1] * n
        self.next = [-1] * n
        self.alive = [False] * n
        self.head = -1
        self.tail = -1
        self.size = 0

        if order is None:
            order = range(n)
        for x in order:
            self.append(x)

    def __len__(self):
        """計算量: 時間・追加空間 O(1)。"""
        return self.size

    def __iter__(self):
        """計算量: 1要素あたり時間 O(1)、全体 O(M)、追加空間 O(1)。M は現在の要素数。"""
        x = self.head
        while x != -1:
            yield x
            x = self.next[x]

    def _check_id(self, x):
        """計算量: 時間・追加空間 O(1)。"""
        if not 0 <= x < len(self.next):
            raise IndexError("node ID is out of range")

    def _check_active(self, x):
        """計算量: 時間・追加空間 O(1)。"""
        self._check_id(x)
        if not self.alive[x]:
            raise ValueError("node is not in the linked list")

    def _check_inactive(self, x):
        """計算量: 時間・追加空間 O(1)。"""
        self._check_id(x)
        if self.alive[x]:
            raise ValueError("node is already in the linked list")

    def append(self, x):
        """リストに含まれていない x を末尾へ追加する。

        計算量: 時間・追加空間 O(1)。
        """
        self._check_inactive(x)

        self.prev[x] = self.tail
        self.next[x] = -1
        if self.tail == -1:
            self.head = x
        else:
            self.next[self.tail] = x
        self.tail = x
        self.alive[x] = True
        self.size += 1

    def appendleft(self, x):
        """リストに含まれていない x を先頭へ追加する。

        計算量: 時間・追加空間 O(1)。
        """
        self._check_inactive(x)

        self.prev[x] = -1
        self.next[x] = self.head
        if self.head == -1:
            self.tail = x
        else:
            self.prev[self.head] = x
        self.head = x
        self.alive[x] = True
        self.size += 1

    def insert_after(self, pos, x):
        """リストに含まれていない x を pos の直後へ追加する。

        計算量: 時間・追加空間 O(1)。
        """
        self._check_active(pos)
        self._check_inactive(x)

        nxt = self.next[pos]
        self.prev[x] = pos
        self.next[x] = nxt
        self.next[pos] = x
        if nxt == -1:
            self.tail = x
        else:
            self.prev[nxt] = x
        self.alive[x] = True
        self.size += 1

    def insert_before(self, pos, x):
        """リストに含まれていない x を pos の直前へ追加する。

        計算量: 時間・追加空間 O(1)。
        """
        self._check_active(pos)
        self._check_inactive(x)

        prv = self.prev[pos]
        self.prev[x] = prv
        self.next[x] = pos
        self.prev[pos] = x
        if prv == -1:
            self.head = x
        else:
            self.next[prv] = x
        self.alive[x] = True
        self.size += 1

    def remove(self, x):
        """x をリストから外す。

        計算量: 時間・追加空間 O(1)。
        """
        self._check_active(x)

        prv = self.prev[x]
        nxt = self.next[x]
        if prv == -1:
            self.head = nxt
        else:
            self.next[prv] = nxt
        if nxt == -1:
            self.tail = prv
        else:
            self.prev[nxt] = prv

        self.prev[x] = -1
        self.next[x] = -1
        self.alive[x] = False
        self.size -= 1

    def move_to_back(self, x):
        """x を末尾へ移動する。

        計算量: 時間・追加空間 O(1)。
        """
        self._check_active(x)
        if x != self.tail:
            self.remove(x)
            self.append(x)

    def move_to_front(self, x):
        """x を先頭へ移動する。

        計算量: 時間・追加空間 O(1)。
        """
        self._check_active(x)
        if x != self.head:
            self.remove(x)
            self.appendleft(x)

    def to_list(self):
        """現在の順序を list で返す。

        計算量: 時間・出力空間 O(M)。M は現在の要素数。
        """
        return list(self)
