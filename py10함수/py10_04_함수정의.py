
# 내장함수

# 사용자함수


strTmp = ""

# 함수에서 입력값은 매개변수로 처리한다.


def get_sum(a, b):
    retSum = 0
    for i in range(a, b+1, 1):
        retSum = retSum + i
    pass

    # strTmp = "%s부터 %s까지의 합계 :: " % (a, b)
    # print(strTmp, retSum)

    return retSum


sum1 = 0
sum2 = 0
sum3 = 0

sum1 = get_sum(1, 10)
strTmp = "%s부터 %s까지의 합계 :: " % (1, 10)
print(strTmp, sum1)

sum2 = get_sum(1, 100)
strTmp = "%s부터 %s까지의 합계 :: " % (1, 100)
print(strTmp, sum2)

sum3 = get_sum(100, sum2)
strTmp = "%s부터 %s까지의 합계 :: " % (100, sum2)
print(strTmp, sum3)
