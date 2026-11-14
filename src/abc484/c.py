import sys
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print("Yes")
    sys.exit()

pref = 0
for i in range(N):
    if A[i] == B[i]:
        pref += 1
    else:
        break

suf = 0
for i in range(N - 1, -1, -1):
    if A[i] == B[i]:
        suf += 1
    else:
        break

A = deque(A[pref : N - suf])
B = deque(B[pref : N - suf])

A.append(A.popleft())
if A == B:
    print("Yes")
    sys.exit()
A.appendleft(A.pop())
A.appendleft(A.pop())
if A == B:
    print("Yes")
    sys.exit()
print("No")
