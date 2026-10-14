# TTSP minimum-cost flow, ACL-Python-like interface.
#
# Copy this whole file above your solution, then use:
#
#   g = MCFGraph(n)
#   g.add_edge(src, dst, cap, cost)
#   flow, cost = g.flow(s, t)
#   points = g.slope(s, t, flow_limit)
#
# This is specialized for directed two-terminal series-parallel networks.
from collections import deque


class NotTTSPError(ValueError):
    """Raised when the input cannot be reduced to one directed TTSP edge."""


class _SlopeTreap:
    """Run-length encoded nondecreasing slopes in an arena treap."""

    __slots__ = (
        "count",
        "free_nodes",
        "lazy_add",
        "left",
        "length",
        "priority",
        "right",
        "rng_state",
        "slope",
        "total_length",
    )

    _MASK64 = (1 << 64) - 1

    def __init__(self) -> None:
        # Node 0 is the empty tree.
        self.left = [0]
        self.right = [0]
        self.priority = [0]
        self.slope = [0]
        self.length = [0]
        self.total_length = [0]
        self.lazy_add = [0]
        self.count = [0]
        self.free_nodes = []
        self.rng_state = 0xD1B54A32D192ED03

    def _next_priority(self) -> int:
        # SplitMix64: deterministic and independent of input keys.
        self.rng_state = (self.rng_state + 0x9E3779B97F4A7C15) & self._MASK64
        value = self.rng_state
        value = ((value ^ (value >> 30)) * 0xBF58476D1CE4E5B9) & self._MASK64
        value = ((value ^ (value >> 27)) * 0x94D049BB133111EB) & self._MASK64
        return (value ^ (value >> 31)) & self._MASK64

    def _new_node(self, slope: int, length: int) -> int:
        assert length > 0
        if self.free_nodes:
            node = self.free_nodes.pop()
            self.left[node] = 0
            self.right[node] = 0
            self.priority[node] = self._next_priority()
            self.slope[node] = slope
            self.length[node] = length
            self.total_length[node] = length
            self.lazy_add[node] = 0
            self.count[node] = 1
            return node

        node = len(self.left)
        self.left.append(0)
        self.right.append(0)
        self.priority.append(self._next_priority())
        self.slope.append(slope)
        self.length.append(length)
        self.total_length.append(length)
        self.lazy_add.append(0)
        self.count.append(1)
        return node

    def _free_node(self, node: int) -> None:
        self.left[node] = 0
        self.right[node] = 0
        self.priority[node] = 0
        self.slope[node] = 0
        self.length[node] = 0
        self.total_length[node] = 0
        self.lazy_add[node] = 0
        self.count[node] = 0
        self.free_nodes.append(node)

    def _pull(self, node: int) -> None:
        left = self.left[node]
        right = self.right[node]
        self.total_length[node] = (
            self.total_length[left] + self.length[node] + self.total_length[right]
        )
        self.count[node] = self.count[left] + 1 + self.count[right]

    def _apply_add(self, node: int, delta: int) -> None:
        if node:
            self.slope[node] += delta
            self.lazy_add[node] += delta

    def _push(self, node: int) -> None:
        delta = self.lazy_add[node]
        if delta:
            self._apply_add(self.left[node], delta)
            self._apply_add(self.right[node], delta)
            self.lazy_add[node] = 0

    def _merge(self, left_root: int, right_root: int) -> int:
        # All slopes in left_root must be <= all slopes in right_root.
        if not left_root:
            return right_root
        if not right_root:
            return left_root

        if self.priority[left_root] > self.priority[right_root]:
            self._push(left_root)
            self.right[left_root] = self._merge(self.right[left_root], right_root)
            self._pull(left_root)
            return left_root

        self._push(right_root)
        self.left[right_root] = self._merge(left_root, self.left[right_root])
        self._pull(right_root)
        return right_root

    def _split_slope(self, root: int, threshold: int) -> tuple[int, int]:
        # (< threshold, >= threshold)
        if not root:
            return 0, 0

        self._push(root)
        if self.slope[root] < threshold:
            middle, right = self._split_slope(self.right[root], threshold)
            self.right[root] = middle
            self._pull(root)
            return root, right

        left, middle = self._split_slope(self.left[root], threshold)
        self.left[root] = middle
        self._pull(root)
        return left, root

    def _split_flow_at_boundary(
        self,
        root: int,
        prefix_length: int,
    ) -> tuple[int, int]:
        # prefix_length is known to be an interval boundary.
        total = self.total_length[root]
        assert 0 <= prefix_length <= total
        if not root:
            return 0, 0
        if prefix_length == 0:
            return 0, root
        if prefix_length == total:
            return root, 0

        self._push(root)
        left_child = self.left[root]
        left_length = self.total_length[left_child]
        own_length = self.length[root]

        if prefix_length < left_length:
            left, middle = self._split_flow_at_boundary(left_child, prefix_length)
            self.left[root] = middle
            self._pull(root)
            return left, root

        if prefix_length > left_length + own_length:
            middle, right = self._split_flow_at_boundary(
                self.right[root],
                prefix_length - left_length - own_length,
            )
            self.right[root] = middle
            self._pull(root)
            return root, right

        if prefix_length == left_length:
            self.left[root] = 0
            self._pull(root)
            return left_child, root

        if prefix_length == left_length + own_length:
            right_child = self.right[root]
            self.right[root] = 0
            self._pull(root)
            return root, right_child

        raise AssertionError("not an interval boundary")

    def _split_flow(self, root: int, prefix_length: int) -> tuple[int, int]:
        # First prefix_length units, and the remainder.  An interval is split
        # into two nodes if the cut lies inside it.
        total = self.total_length[root]
        assert 0 <= prefix_length <= total
        if not root:
            return 0, 0
        if prefix_length == 0:
            return 0, root
        if prefix_length == total:
            return root, 0

        current = root
        amount_before_subtree = 0
        while current:
            self._push(current)
            left_length = self.total_length[self.left[current]]
            interval_start = amount_before_subtree + left_length
            interval_end = interval_start + self.length[current]

            if prefix_length < interval_start:
                current = self.left[current]
                continue
            if prefix_length > interval_end:
                amount_before_subtree = interval_end
                current = self.right[current]
                continue

            offset = prefix_length - interval_start
            if offset == 0 or offset == self.length[current]:
                return self._split_flow_at_boundary(root, prefix_length)

            old_length = self.length[current]
            old_slope = self.slope[current]

            left_tree, rest = self._split_flow_at_boundary(root, interval_start)
            isolated, right_tree = self._split_flow_at_boundary(rest, old_length)
            assert self.count[isolated] == 1

            self._push(isolated)
            self.length[isolated] = offset
            self._pull(isolated)
            right_piece = self._new_node(old_slope, old_length - offset)

            return (
                self._merge(left_tree, isolated),
                self._merge(right_piece, right_tree),
            )

        raise AssertionError("flow split failed")

    def _insert_segment(self, root: int, slope: int, length: int) -> int:
        left, right = self._split_slope(root, slope)
        node = self._new_node(slope, length)
        return self._merge(self._merge(left, node), right)

    def _recycle_subtree(self, root: int) -> None:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            left = self.left[node]
            right = self.right[node]
            if left:
                stack.append(left)
            if right:
                stack.append(right)
            self._free_node(node)

    def _flatten_and_recycle(self, root: int) -> list[tuple[int, int]]:
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                self._push(current)
                stack.append(current)
                current = self.left[current]

            current = stack.pop()
            slope = self.slope[current]
            length = self.length[current]
            next_node = self.right[current]

            if result and result[-1][0] == slope:
                result[-1] = (slope, result[-1][1] + length)
            else:
                result.append((slope, length))

            self._free_node(current)
            current = next_node

        return result

    def make_segment(self, cap: int, cost: int) -> int:
        if cap == 0:
            return 0
        return self._new_node(cost, cap)

    def parallel(self, first: int, second: int) -> int:
        if not first:
            return second
        if not second:
            return first

        if self.count[first] < self.count[second]:
            first, second = second, first

        for slope, length in self._flatten_and_recycle(second):
            first = self._insert_segment(first, slope, length)
        return first

    def series(self, first: int, second: int) -> int:
        if not first or not second:
            self._recycle_subtree(first)
            self._recycle_subtree(second)
            return 0

        cap = min(
            self.total_length[first],
            self.total_length[second],
        )
        first, first_suffix = self._split_flow(first, cap)
        second, second_suffix = self._split_flow(second, cap)
        self._recycle_subtree(first_suffix)
        self._recycle_subtree(second_suffix)

        if self.count[first] < self.count[second]:
            first, second = second, first

        smaller = self._flatten_and_recycle(second)
        remaining = first
        result = 0
        for slope, length in smaller:
            prefix, remaining = self._split_flow(remaining, length)
            self._apply_add(prefix, slope)
            result = self._merge(result, prefix)

        assert remaining == 0
        return result

    def segments(self, root: int) -> list[tuple[int, int]]:
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                self._push(current)
                stack.append(current)
                current = self.left[current]

            current = stack.pop()
            slope = self.slope[current]
            length = self.length[current]
            if result and result[-1][0] == slope:
                result[-1] = (slope, result[-1][1] + length)
            else:
                result.append((slope, length))
            current = self.right[current]

        return result


def _solve_ttsp(
    n: int,
    edge_src: list[int],
    edge_dst: list[int],
    edge_cap: list[int],
    edge_cost: list[int],
    source: int,
    sink: int,
) -> list[tuple[int, int]]:
    m = len(edge_src)
    if m == 0:
        raise NotTTSPError("the graph has no edges")

    used_vertex = [False] * n
    for edge_id in range(m):
        src = edge_src[edge_id]
        dst = edge_dst[edge_id]
        if src == dst:
            raise NotTTSPError("self-loops are not TTSP edges")
        used_vertex[src] = True
        used_vertex[dst] = True

    if not used_vertex[source] or not used_vertex[sink]:
        raise NotTTSPError("source and sink must be incident to the graph")

    treap = _SlopeTreap()

    # One entry per temporary SP component.
    tails = []
    heads = []
    tree_roots = []
    alive = []
    next_in = []
    next_out = []

    # Lazy incidence linked lists. Dead components remain linked and are
    # skipped only when a degree-1 vertex needs its sole live component.
    in_head = [-1] * n
    out_head = [-1] * n
    in_degree = [0] * n
    out_degree = [0] * n

    pair_component = {}
    queue = deque()
    queued = [False] * n
    eliminated = [False] * n
    active_count = 0

    def enqueue(vertex: int) -> None:
        if vertex == source or vertex == sink or eliminated[vertex]:
            return
        if not queued[vertex]:
            queued[vertex] = True
            queue.append(vertex)

    def create_component(tail: int, head: int, tree_root: int) -> int:
        component = len(tails)
        tails.append(tail)
        heads.append(head)
        tree_roots.append(tree_root)
        alive.append(False)
        next_in.append(-1)
        next_out.append(-1)
        return component

    def activate(component: int) -> None:
        nonlocal active_count
        assert not alive[component]
        alive[component] = True
        active_count += 1

        tail = tails[component]
        head = heads[component]
        next_out[component] = out_head[tail]
        out_head[tail] = component
        out_degree[tail] += 1
        next_in[component] = in_head[head]
        in_head[head] = component
        in_degree[head] += 1
        pair_component[(tail, head)] = component
        enqueue(tail)
        enqueue(head)

    def deactivate(component: int) -> None:
        nonlocal active_count
        assert alive[component]
        alive[component] = False
        active_count -= 1

        tail = tails[component]
        head = heads[component]
        out_degree[tail] -= 1
        in_degree[head] -= 1
        key = (tail, head)
        if pair_component.get(key) == component:
            del pair_component[key]
        enqueue(tail)
        enqueue(head)

    def register(component: int) -> int:
        # COMPONENT is new and not linked to incidence lists yet.
        assert not alive[component]
        tail = tails[component]
        head = heads[component]
        existing = pair_component.get((tail, head))

        if existing is not None:
            deactivate(existing)
            merged_root = treap.parallel(tree_roots[existing], tree_roots[component])
            tree_roots[existing] = 0
            tree_roots[component] = 0
            merged = create_component(tail, head, merged_root)
            return register(merged)

        activate(component)
        return component

    def sole_incoming(vertex: int) -> int:
        component = in_head[vertex]
        while component != -1 and not alive[component]:
            component = next_in[component]
        in_head[vertex] = component
        assert component != -1
        return component

    def sole_outgoing(vertex: int) -> int:
        component = out_head[vertex]
        while component != -1 and not alive[component]:
            component = next_out[component]
        out_head[vertex] = component
        assert component != -1
        return component

    for edge_id in range(m):
        component = create_component(
            edge_src[edge_id],
            edge_dst[edge_id],
            treap.make_segment(edge_cap[edge_id], edge_cost[edge_id]),
        )
        register(component)

    for vertex in range(n):
        enqueue(vertex)

    while queue:
        vertex = queue.popleft()
        queued[vertex] = False
        if eliminated[vertex] or vertex == source or vertex == sink:
            continue
        if in_degree[vertex] != 1 or out_degree[vertex] != 1:
            continue

        first = sole_incoming(vertex)
        second = sole_outgoing(vertex)
        if first == second:
            raise NotTTSPError("a directed cycle blocks TTSP reduction")
        assert heads[first] == vertex and tails[second] == vertex

        tail = tails[first]
        head = heads[second]
        if tail == head:
            raise NotTTSPError("series reduction creates a cycle")

        deactivate(first)
        deactivate(second)
        eliminated[vertex] = True
        merged_root = treap.series(tree_roots[first], tree_roots[second])
        tree_roots[first] = 0
        tree_roots[second] = 0
        merged = create_component(tail, head, merged_root)
        register(merged)

    root = pair_component.get((source, sink))
    if root is None or active_count != 1 or not alive[root]:
        raise NotTTSPError(
            "the graph cannot be reduced to one source-to-sink component"
        )

    for vertex in range(n):
        if (
            used_vertex[vertex]
            and vertex != source
            and vertex != sink
            and not eliminated[vertex]
        ):
            raise NotTTSPError(
                f"vertex {vertex} cannot be eliminated by TTSP reductions"
            )

    return treap.segments(tree_roots[root])


class MCFGraph:
    """ACL-Python-like min-cost-flow interface specialized for directed TTSP.

    Core signatures intentionally match ``atcoder.mincostflow.MCFGraph``:

    * ``MCFGraph(n)``
    * ``add_edge(src, dst, cap, cost)``
    * ``flow(s, t, flow_limit=None)``
    * ``slope(s, t, flow_limit=None)``

    Differences from ACL's general residual-network implementation:

    * the graph must be a directed two-terminal series-parallel network;
    * ``flow`` and ``slope`` do not mutate the graph, so repeated calls are OK;
    * per-edge flow reconstruction is not implemented, so ACL's
      ``get_edge`` / ``edges`` methods are intentionally omitted.
    """

    def __init__(self, n: int) -> None:
        assert 0 <= n
        self._n = n
        self._src = []  # type: typing.List[int]
        self._dst = []  # type: typing.List[int]
        self._cap = []  # type: typing.List[int]
        self._cost = []  # type: typing.List[int]
        self._cache_st = None  # type: typing.Optional[typing.Tuple[int, int]]
        self._cache_segments = None  # type: typing.Optional[typing.List[typing.Tuple[int, int]]]

    def add_edge(self, src: int, dst: int, cap: int, cost: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        edge_id = len(self._src)
        self._src.append(src)
        self._dst.append(dst)
        self._cap.append(cap)
        self._cost.append(cost)
        self._cache_st = None
        self._cache_segments = None
        return edge_id

    def _segments(self, s: int, t: int) -> list[tuple[int, int]]:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t

        if self._cache_st == (s, t):
            assert self._cache_segments is not None
            return self._cache_segments

        segments = _solve_ttsp(
            self._n,
            self._src,
            self._dst,
            self._cap,
            self._cost,
            s,
            t,
        )
        self._cache_st = (s, t)
        self._cache_segments = segments
        return segments

    def flow(
        self,
        s: int,
        t: int,
        flow_limit: int | None = None,
    ) -> tuple[int, int]:
        return self.slope(s, t, flow_limit)[-1]

    def slope(
        self,
        s: int,
        t: int,
        flow_limit: int | None = None,
    ) -> list[tuple[int, int]]:
        segments = self._segments(s, t)
        maximum_flow = sum(length for _, length in segments)

        if flow_limit is None:
            flow_limit = maximum_flow
        assert 0 <= flow_limit
        flow_limit = min(flow_limit, maximum_flow)

        result = [(0, 0)]
        flow = 0
        cost = 0
        for unit_cost, amount in segments:
            take = min(amount, flow_limit - flow)
            if take <= 0:
                break
            flow += take
            cost += take * unit_cost
            result.append((flow, cost))
            if flow == flow_limit:
                break
        return result

    def marginal_costs(self, s: int, t: int) -> list[tuple[int, int]]:
        """Return ``(unit_cost, amount)`` runs used internally by the DP."""
        return list(self._segments(s, t))
