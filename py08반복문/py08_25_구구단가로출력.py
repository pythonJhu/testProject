
guguStr = ""
for x in range(2, 20, 1):
    for y in range(1, 10, 1):
        guguStr = "%s * %s = %s" % (x, y,  x * y)  # %2s, %3s 는 자리수를 맞추기 위해서
        if y == 9:
            print(guguStr, end=".")
        else:
            print(guguStr, end=",")
    print()
