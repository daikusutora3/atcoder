N = int(input())
ABC = list(map(int, input().split()))
ABC.sort()

A, B, C = ABC[0], ABC[1], ABC[2]

n = N
ans_C = 0
for i in range(10**4):
    if n < 0:
        break
    if i == 44:
        print(n, (n % B) % A)
    if (n % B) % A == 0:
        ans_C = i
    n -= C

n = N - ans_C * C
print("Cの金額と硬貨の枚数:", n, ans_C)
ans_B = n // B
n = n - ans_B * B
print("Bの金額と硬貨の枚数:", n, ans_B)
ans_A = n // A
ans = ans_C + ans_B + ans_A
print("Aの金額と硬貨の枚数:", n, ans_A)

print(ans)
