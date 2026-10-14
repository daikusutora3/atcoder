N = int(input())

cnt3 = N // 3
cnt5 = N // 5
cnt7 = N // 7
cnt15 = N // 15
cnt21 = N // 21
cnt35 = N // 35
cnt105 = N // 105

print(cnt3 + cnt5 + cnt7 - cnt15 - cnt21 - cnt35 + cnt105)
