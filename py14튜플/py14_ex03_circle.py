import math  # PI = 3.14... 변수를 사용하기 위해서 import


def getCircle(radius):
    면적 = math.pi * radius * radius
    둘레 = 2 * math.pi * radius
    return (면적, 둘레)


def main():
    str = input("원의 반지금 입력 : ")
    radius = float(str)  # 문자열을 실수로 변환 한다.
    # 원의 넓이와 둘레를 계산한다.

    (x, y) = getCircle(radius)

    tmp = "원의 넓이 %10.4f , 둘레는 %10.4f 이다" % (x, y)
    print(tmp)


if __name__ == "__main__":
    main()
