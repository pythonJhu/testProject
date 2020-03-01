# -*- coding: utf-8 -*-


# 도전 2. 형변환. 문자열을 정수로 바꾸기.
# 문자열 "3"을 정수 3으로 바꾸시오. 구글 검색
# temp2 = "3"

# 도전 3. 문자열에서 가장 큰 수를 찾으시오.
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트에서 최대값을 찾는다.


def getNumList(strTmp):
    pass

    strArr = strTmp.split(" ")

    idx = 0
    numList = []
    for i in strArr:
        try:
            n = int(i)
            # print(idx, n, end="\n")
            numList.append(n)

            idx += 1
        except ValueError as ex:
            print(ex)

    return numList


def main():
    strTmp = "1 2 879 3 4 11 134135 567 256 55"

    arr = getNumList(strTmp)
    descArr = sorted(arr)
    maxNum = max(descArr)
    print("max ::: ", maxNum)
    print("idx :: ", descArr[len(descArr) - 1])


main()
