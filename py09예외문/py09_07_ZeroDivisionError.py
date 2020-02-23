num1 = input("숫자1 입력 : ")
num2 = input("숫자2 입력 : ")

try:
    num1 = int(num1)
    num2 = int(num2)

    res = num1 / num2
except ValueError as ex:
    print("ValueError :: ", ex)  # 로그 파일에 저장하는 방식으로 수정 필요
except ZeroDivisionError as ex:
    print("ZeroDivisionError :: ", ex)
