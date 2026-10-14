X = list(map(int, input()))

X.sort()
ans = ""
zero_count = X.count(0)
ans += str(X[zero_count])
ans += "0" * zero_count
for a in X[zero_count + 1 :]:
    ans += str(a)

print(ans)
