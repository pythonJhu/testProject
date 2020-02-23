# 왜 반복이 사용하나?


# 순차문

# print("just print :: ", "환영합니다.\n환영합니다.\n환영합니다.\n환영합니다.\n환영합니다.)

# for문

for x in range(0, 5, 1):
    srtTmp = "%s :: 환영합니다." % (x)
    print("for :: ", srtTmp)

# while문

x = 0
while x < 5:
    srtTmp = "%s :: 환영합니다." % (x)
    print("while :: ", srtTmp)
    x += 1
