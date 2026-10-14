S = input()

ans = 0
for i in range(len(S) - 1):
    left = i
    right = left + 1
    while (
        (left >= 0 and right < len(S))
        and int(S[i]) == int(S[left])
        and int(S[left]) + 1 == int(S[right])
    ):
        ans += 1
        left -= 1
        right += 1

print(ans)
