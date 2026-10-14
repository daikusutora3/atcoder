N = int(input())
S = input()

flag = True
for s in S:
    if flag and s == "o":
        continue
    else:
        flag = False
    print(s, end="")
print()
