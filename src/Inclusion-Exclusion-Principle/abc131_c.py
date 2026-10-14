from math import lcm


A, B, C, D = map(int, input().split())
cntC = B // C - (A - 1) // C
cntD = B // D - (A - 1) // D
cntCD = B // lcm(C, D) - (A - 1) // lcm(C, D)

print(B - A + 1 - cntC - cntD + cntCD)
