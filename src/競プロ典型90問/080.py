N, D = map(int, input().split())
A = list(map(int, input().split()))


ans = 0
for bit in range(2**N):
    if bit.bit_count() == 0:
        continue
    or_bit = 0
    for i in range(N):
        if bit >> i & 1:
            or_bit |= A[i]
    cnt = or_bit.bit_count()
    # print(bin(bit), bin(or_bit), pow(2, D - cnt), bit.bit_count() % 2)
    ans += pow(2, D - cnt) * (1 if bit.bit_count() % 2 else -1)

print(pow(2, D) - ans)
