N = int(input())
A = list(map(int, input().split()))
print(max(A) if A.count(max(A)) == 1 else 0)
