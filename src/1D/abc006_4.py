import bisect

N = int(input())
seq = []
for i in range(N):
    c = int(input())
    seq.append(c - 1)


LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(N - len(LIS))
