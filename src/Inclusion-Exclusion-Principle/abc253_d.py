from math import lcm


def f(x):
    return x * (x + 1) // 2


N, A, B = map(int, input().split())

print(f(N) - A * f(N // A) - B * f(N // B) + lcm(A, B) * f(N // lcm(A, B)))
