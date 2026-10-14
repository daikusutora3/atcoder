A, B = map(int, input().split())


if ((A + B) == 9) or ((A - B) == 9) or ((A * B) == 9) or ((A // B) == 9 and A % 9 == 0):
    print("Nine")
else:
    print("Nein")
