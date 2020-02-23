# while 문을 사용하여 1부터 100 사이의 3의 배수의 합을 계산하여 출력 하시오

# x = 3
# sumX = 0
# while x <= 100:
#     print(x)
#     sumX += x
#     x += 3

# print("합계", sumX)


x = 1
sumX = 0
while x <= 100:

    if 0 == x % 3:
        print(x)
        sumX += x
    else:
        pass

    x += 1

print("합계", sumX)
