A, B, C = map(int, input().split())

data = [A, B, C]
data.sort(reverse=True)
# print(data)
for a in data:
    print(a, end="")
print()
