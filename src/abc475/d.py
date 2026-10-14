import sys
from itertools import permutations


def sieve_primes(n):
    """n 以下の素数リストを返す。"""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]


primes = sieve_primes(10**7 + 1)


primes = set(primes)

S = input()
moji = list(set(S))
moji.sort()
for comb in permutations(list(range(10)), len(moji)):
    d = {}
    for i in range(len(moji)):
        d[moji[i]] = str(comb[i])
    res = []
    for s in S:
        res.append(d[s])
    if res[0] == "0":
        continue
    ans = int("".join(res))
    if ans in primes:
        print(ans)
        sys.exit()

print(-1)
