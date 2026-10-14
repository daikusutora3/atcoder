N, M = map(int, input().split())
S = input()
T = input()
S_set = set()
T_set = set()
for s in S:
    S_set.add(s)
for t in T:
    T_set.add(t)

Q = int(input())

for _ in range(Q):
    W = input()
    W_set = set()
    for w in W:
        W_set.add(w)
    if S_set >= W_set and (not T_set >= W_set):
        print("Takahashi")
    elif T_set >= W_set and (not S_set >= W_set):
        print("Aoki")
    else:
        print("Unknown")
