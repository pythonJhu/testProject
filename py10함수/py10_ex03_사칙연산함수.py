def Add(firstNum, secondNum):
    result = firstNum + secondNum
    return result


def Minus(firstNum, secondNum):
    # minNum = min(firstNum, secondNum)
    # maxNum = max(firstNum, secondNum)

    # result = maxNum - minNum
    # return result

    result = firstNum - secondNum
    return result


def Mul(firstNum, secondNum):
    result = firstNum * secondNum
    return result


def Div(firstNum, secondNum):
    result = firstNum / secondNum
    return result

    # try:
    #     result = firstNum / secondNum
    # except ZeroDivisionError as ex:
    #     print("ZeroDivisionError :: ", ex)
    # pass


x = input("First Num :: ")
y = input("Second Num :: ")

# 문자열 정수 변환
x = int(x)
y = int(y)

# Add 함수 호출
value = Add(x, y)
print("Add :: ", value)
# Minus 함수 호출
value = Minus(x, y)
print("Minus :: ", value)
# Mul 함수 호출
value = Mul(x, y)
print("Mul :: ", value)
# Div 함수 호출
value = Div(x, y)
print("Div :: ", value)
