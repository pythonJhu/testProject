# 중첩 for문

for x in range(2, 20, 1):
    print(x, "단")
    for y in range(1, 10, 1):
        gugu = x * y
        print(x, " / ", y, " == ", gugu)
        pass
    pass
