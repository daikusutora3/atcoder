class Trie:
    def __init__(self):
        # next[v] := 頂点 v から文字 c で進む先
        self.next = [{}]

        # pass_count[v] := 頂点 v を通る文字列の個数
        self.pass_count = [0]

        # end_count[v] := 頂点 v で終わる文字列の個数
        self.end_count = [0]

    def insert(self, s):
        """
        文字列 s を1個追加する。
        計算量: O(len(s))
        """
        v = 0
        self.pass_count[v] += 1

        for c in s:
            if c not in self.next[v]:
                self.next[v][c] = len(self.next)
                self.next.append({})
                self.pass_count.append(0)
                self.end_count.append(0)

            v = self.next[v][c]
            self.pass_count[v] += 1

        self.end_count[v] += 1

    def delete(self, s):
        """
        文字列 s を1個削除する。

        s が存在すれば True、
        存在しなければ False を返す。

        計算量: O(len(s))
        """
        v = 0
        path = [0]

        # s の終点まで辿る
        for c in s:
            if c not in self.next[v]:
                return False

            v = self.next[v][c]
            path.append(v)

        # s 自体が登録されていない
        if self.end_count[v] == 0:
            return False

        # 1個削除
        self.end_count[v] -= 1

        for v in path:
            self.pass_count[v] -= 1

        return True

    def count(self, s):
        """
        文字列 s が何個登録されているか返す。
        計算量: O(len(s))
        """
        v = 0

        for c in s:
            if c not in self.next[v]:
                return 0
            v = self.next[v][c]

        return self.end_count[v]

    def contains(self, s):
        """
        文字列 s が登録されているか。
        計算量: O(len(s))
        """
        return self.count(s) > 0

    def prefix_count(self, prefix):
        """
        prefix から始まる文字列が何個あるか返す。
        計算量: O(len(prefix))
        """
        v = 0

        for c in prefix:
            if c not in self.next[v]:
                return 0
            v = self.next[v][c]

        return self.pass_count[v]

    def starts_with(self, prefix):
        """
        prefix から始まる文字列が存在するか。
        計算量: O(len(prefix))
        """
        return self.prefix_count(prefix) > 0

    def size(self):
        """
        登録されている文字列の総数。
        重複を含む。
        """
        return self.pass_count[0]

    def node_count(self):
        """
        Trie 木に作られた頂点数。
        削除済みノードも含む。
        """
        return len(self.next)


trie = Trie()
N, M, K = map(int, input().split())
T = input()

X = [["0" for k in range(K)] for i in range(N)]
for i in range(N):
    S = input()
    for k in range(K):
        if S[k] == T[k]:
            X[i][k] = "0"
        else:
            X[i][k] = "1"
    trie.insert("".join(X[i]))

Q = int(input())
for _ in range(Q):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    trie.delete("".join(X[i]))
    X[i][j] = "0" if X[i][j] == "1" else "1"
    trie.insert("".join(X[i]))
    now = []
    cnt = M
    for k in range(K):
        z = trie.prefix_count("".join(now + ["0"]))
        if z > cnt:
            now.append("0")
        else:
            cnt -= z
            now.append("1")
    if len(X[i]) == len(now) and "".join(X[i]) < "".join(now):
        print("Yes")
    else:
        print("No")
