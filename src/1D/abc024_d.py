mod = 10**9 + 7
A = int(input())
B = int(input())
C = int(input())

r = ((B * C - A * C) * pow(A * C - B * C + A * B, mod - 2, mod)) % mod
c = ((B * C - A * B) * pow(A * B - B * C + A * C, mod - 2, mod)) % mod
print(r, c)
