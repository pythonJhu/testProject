
# step1. ArrayList 인스턴스, list  만들기.
# step2. 심사 위원수를 입력 받는다.
# step3. 심사 위원의 점수 입력 받아서 list에 저장.
#     몇 번 입력 받아야 하는가? 심사 위원수 만큼
# step4. 합계를 구하는 메서드 만들기
#     1번방부터 마지막방 -1 까지
# step5. 평균을 구하는 메서드 만들기.
#     평균값 = (double)sum / ( list.size() - 2 )
# step6. ArrayLis 정렬하기.
# step7. 합계를 구하고 출력한다.
# step8. 평균을 구하고 출력한다.


def getSum(pList):
    result = 0

    pList = sorted(pList)
    idx = 0
    print(len(pList), " === ", pList)
    for x in pList:

        if idx == 0 or idx == len(pList)-1:
            pass
        else:
            print(idx, "===", x)
            result = result + x

        idx += 1
    print("getSum result == ", result)
    return result


def main():

    strCnt = input("심사 위원수 = ")

    try:
        iCnt = int(strCnt)
    except ValueError as ex:
        print(ex)

    pList = []
    for i in range(0, iCnt, 1):
        try:
            p = int(input("심사위원 점수 입력 = "))
            pList.append(p)
        except ValueError as ex:
            print(ex)

    sumPoint = getSum(pList)
    svgPoint = float(sumPoint / len(pList))

    tmp = "합계 = %s / 평균 = %s" % (sumPoint, svgPoint)
    print(tmp)


if __name__ == "__main__":
    main()
