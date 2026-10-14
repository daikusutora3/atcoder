N, K = map(int, input().split())

wp = [list(map(int, input().split())) for i in range(N)]


def is_ok(k):
    # kパーセント以上が可能ですか？
    global N, K, wp
    st = []
    for w, p in wp:
        st.append(w * p / 100 - w * k / 100)
    st.sort(reverse=True)
    return sum(st[:K]) >= 0


ok, ng = 0, 100

while abs(ng - ok) > (1 / 10**6):
    mid = (ok + ng) / 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
