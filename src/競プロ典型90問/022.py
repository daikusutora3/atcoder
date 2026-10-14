from math import gcd


A, B, C = map(int, input().split())

g = gcd(A, B, C)

print(A // g + B // g + C // g - 3)
