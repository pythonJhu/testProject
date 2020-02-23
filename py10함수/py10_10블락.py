def get_sum(a, b):
    retSum = 0
    for i in range(a, b+1, 1):
        retSum = retSum + i
        pass

    strTmp = "%s부터 %s까지의 합계 :: " % (a, b)
    print(strTmp, retSum)

    # return retSum


x = 3
y = 7
get_sum(x, y)

# 전역변수 : x, y
# 매개변수 : a, b
# 지역변수 : i, retSum, a, b
