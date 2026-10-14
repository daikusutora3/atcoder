Q = int(input())
play = False
volume = 0

for _ in range(Q):
    a = int(input())
    if a == 1:
        volume += 1
    elif a == 2:
        volume = max(0, volume - 1)
    else:
        play = not play
    if play and volume >= 3:
        print("Yes")
    else:
        print("No")
