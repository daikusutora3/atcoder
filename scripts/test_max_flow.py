import sys, random, runpy, io, contextlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from library.graph.max_flow import MFGraph
from library.graph.bipartite_matching import BipartiteMatching, bipartite_matching
assert (ROOT / 'library/graph/bipartite_matching.py').read_text() in (ROOT / 'src/flow/typical90_by.py').read_text()
rng = random.Random(77)
for case in range(2000):
    n = rng.randrange(2, 9)
    es = [(rng.randrange(n), rng.randrange(n), rng.randrange(10)) for _ in range(rng.randrange(40))]
    g = MFGraph(n)
    for u, v, c in es:
        g.add_edge(u, v, c)
    expected = min(sum(c for u, v, c in es if (mask >> u & 1) and not (mask >> v & 1)) for mask in range(1 << n) if mask & 1 and not(mask >> (n-1) & 1))
    lim = rng.randrange(15)
    f = g.flow(0, n-1, lim)
    assert f == min(expected, lim), (case, es, f, expected, lim)
    assert f + g.flow(0, n-1) == expected
    assert g.flow(0, n-1) == 0
    cut = g.min_cut(0)
    assert sum(c for u,v,c in es if cut[u] and not cut[v]) == expected
    balance = [0] * n
    for i, e in enumerate(g.edges()):
        assert (e.src, e.dst, e.cap) == es[i]
        assert 0 <= e.flow <= e.cap and e.flow == g.edge_flow(i)
        balance[e.src] -= e.flow
        balance[e.dst] += e.flow
    assert balance == [-expected] + [0]*(n-2) + [expected]
# Deep paths, large capacities, parallel and reverse edges are covered above.
g = MFGraph(50000)
for i in range(49999): g.add_edge(i, i+1, 10**40)
assert g.flow(0, 49999) == 10**40
g = MFGraph(2)
g.add_edge(0, 1, 3)
assert g.flow(0,1) == 3
g.add_edge(0,1,5)
assert g.flow(0,1) == 5
print('max flow: 2000 exhaustive min-cut comparisons, flow limits, conservation, deep path passed')
ns = runpy.run_path(str(ROOT / 'src/flow/typical90_by.py'))
moves = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
def solve(a,b,t):
    data = f'{len(a)} {t}\n' + ''.join(f'{x} {y}\n' for x,y in a+b)
    old = sys.stdin
    sys.stdin = io.TextIOWrapper(io.BytesIO(data.encode()))
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out): ns['main']()
    finally: sys.stdin = old
    return out.getvalue().split()
for case in range(500):
    n = rng.randrange(1,9)
    t = rng.randrange(1,4)
    coords = [(x,y) for x in range(6) for y in range(6)]
    a = rng.sample(coords,n)
    b = rng.sample(coords,n)
    states = {0}
    for x,y in a:
        js = [j for j,(bx,by) in enumerate(b) if (bx-x,by-y) in [(dx*t,dy*t) for dx,dy in moves]]
        states = {mask | (1<<j) for mask in states for j in js if not(mask >> j & 1)}
    out = solve(a,b,t)
    assert (out[0] == 'Yes') == bool(states)
    if states:
        assert len(out) == n+1
        result = [(x+moves[int(d)-1][0]*t,y+moves[int(d)-1][1]*t) for (x,y),d in zip(a,out[1:])]
        assert sorted(result) == sorted(b)
print('solver: 500 random cases versus subset DP, directions validated')

assert solve([(3, 3), (5, 5), (9, 2)], [(11, 2), (5, 5), (3, 3)], 2) == ['Yes', '2', '6', '1']
assert solve([(3, 3), (5, 5), (9, 2)], [(11, 10**9), (5, 5), (3, 3)], 2) == ['No']
# 候補は全頂点にあるが Hall 条件を満たさない。
assert solve([(0, 0), (0, 2)], [(1, 1), (9, 9)], 1) == ['No']
assert solve([(0, 0)], [(10**9, 10**9)], 10**9) == ['Yes', '2']
print('samples 1/2, Hall obstruction, coordinate boundary passed')

sample3 = '''540130346 269080121
139837096 165633078
731188937 784167460
18996195 52176517
153153670 738204723
179733158 825294112
698198250 713974773
449248931 563096572
249863070 242694893
428066819 476630383
554127636 460973490
389988495 32320086
889782910 956212985
43905938 212030305
638141790 667879166
985957895 358743012
971007109 827787244
804625543 141347414
905270323 167192824
614855582 963943648
179733932 825294886
731188163 784166686
153154444 738205497
554128410 460973490
804626317 141348188
449249705 563096572
540129572 269079347
638142564 667878392
614855582 963944422
18996969 52177291
971007109 827788018
889782910 956213759
43906712 212031079
389987721 32319312
139836322 165633078
428067593 476631157
905271097 167192824
249862296 242694893
985958669 358742238
698199024 713975547'''
coords = [tuple(map(int, row.split())) for row in sample3.splitlines()]
a, b = coords[:20], coords[20:]
out = solve(a, b, 774)
assert out[0] == 'Yes' and len(out) == 21
result = [(x + moves[int(d)-1][0]*774, y + moves[int(d)-1][1]*774)
          for (x, y), d in zip(a, out[1:])]
assert sorted(result) == sorted(b)
print('sample 3 passed')

for case in range(1500):
    n, m = rng.randrange(8), rng.randrange(8)
    adj = [[v for v in range(m) if rng.randrange(2)] for _ in range(n)]
    if n and adj[0]:
        adj[0] += adj[0]  # 重複辺も許す。
    states = {0}
    for row in adj:
        states |= {mask | (1 << v) for mask in states for v in row if not (mask >> v & 1)}
    expected = max(bin(mask).count('1') for mask in states)
    result = bipartite_matching(adj, m)
    chosen = [v for v in result if v >= 0]
    assert len(chosen) == len(set(chosen)) == expected
    assert all(v == -1 or v in adj[u] for u, v in enumerate(result))
    graph = BipartiteMatching(n, m)
    for u, row in enumerate(adj):
        for v in row:
            graph.add_edge(u, v)
    assert graph.solve() == expected
    pairs = graph.pairs()
    assert len(pairs) == expected
    assert len({u for u, v in pairs}) == len({v for u, v in pairs}) == expected
    assert all(v in adj[u] for u, v in pairs)
n = 50000
adj = [[u, u+1] for u in range(n-1)] + [[0]]
result = bipartite_matching(adj, n)
assert len(set(result)) == n and -1 not in result
assert result == list(range(1, n)) + [0]
print('matching: 1500 subset-DP comparisons and 50000-vertex alternating path passed')

graph = BipartiteMatching(2, 2)
graph.add_edge(0, 0)
graph.add_edge(1, 0)
assert len(graph.pairs()) == 1  # solve 前でも取得できる。
assert graph.solve() == graph.solve() == 1
graph.add_edge(0, 1)  # 既存の組を組み替える必要がある。
assert graph.solve() == 2
assert graph.pairs() == [(0, 1), (1, 0)]
pairs = graph.pairs()
pairs.clear()
assert graph.pairs() == [(0, 1), (1, 0)]
assert BipartiteMatching(0, 3).pairs() == []
print('class API: repeated solve, edge addition, pairs before solve, empty graph passed')
