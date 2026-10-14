def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


K = int(input())
divs = make_divisors(K)

ans = 0
for i, a in enumerate(divs):
    if a**3 > K:
        break
    for b in divs[i:]:
        if K % (a * b) != 0:
            continue
        c = K // (a * b)
        if b > c:
            break
        ans += 1

print(ans)
