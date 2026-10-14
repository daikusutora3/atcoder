import bisect

N = int(input())
wh = [list(map(int, input().split())) for i in range(N)]

wh.sort(key=lambda x: (x[0], -x[1]))

seq = []
for w, h in wh:
    seq.append(h)


LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS))
