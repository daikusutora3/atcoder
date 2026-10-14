N, K = map(int, input().split())
A = list(map(int, input().split()))
tak = 0
for i in range(N):
    if tak + A[i] <= K:
        tak += A[i]

aok = sum(A) - tak

if aok == tak:
    print("Draw")
elif aok > tak:
    print("Aoki")
else:
    print("Takahashi")
