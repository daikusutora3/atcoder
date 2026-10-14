class IndexLinkedList:
    """0..n-1 の整数をノード ID として扱う双方向連結リスト。"""

    def __init__(self, n, order=None):
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
        return self.size

    def __iter__(self):
        x = self.head
        while x != -1:
            yield x
            x = self.next[x]

    def _check_id(self, x):
        if not 0 <= x < len(self.next):
            raise IndexError("node ID is out of range")

    def _check_active(self, x):
        self._check_id(x)
        if not self.alive[x]:
            raise ValueError("node is not in the linked list")

    def _check_inactive(self, x):
        self._check_id(x)
        if self.alive[x]:
            raise ValueError("node is already in the linked list")

    def append(self, x):
        """リストに含まれていない x を末尾へ追加する。"""
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
        """リストに含まれていない x を先頭へ追加する。"""
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
        """リストに含まれていない x を pos の直後へ追加する。"""
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
        """リストに含まれていない x を pos の直前へ追加する。"""
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
        """x をリストから外す。"""
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
        """x を末尾へ移動する。"""
        self._check_active(x)
        if x != self.tail:
            self.remove(x)
            self.append(x)

    def move_to_front(self, x):
        """x を先頭へ移動する。"""
        self._check_active(x)
        if x != self.head:
            self.remove(x)
            self.appendleft(x)

    def to_list(self):
        """現在の順序を list で返す。"""
        return list(self)
