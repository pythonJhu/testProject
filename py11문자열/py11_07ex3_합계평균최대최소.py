
def getList(tmp):
    arr = tmp.split(" ")

    numArr = []
    try:
        for i in arr:
            n = int(i)
            numArr.append(n)

        return numArr

    except ValueError as ex:
        print(ex)


def main():
    numStr = "70 71 72 82 95 100 45 68 96 36 77 54 68"

    rArr = getList(numStr)
    # print("rArr ::: ", rArr[0])
    # nSum = 0
    arrLen = len(rArr)
    # for x in rArr:
    #     nSum = nSum + x

    # nSum = sum(rArr)

    # asclist = sorted(rArr)
    print("길이 :: ", arrLen)
    print("최대 :: ", max(rArr))
    print("최소 ::", min(rArr))
    print("합계 :: ", sum(rArr))
    print("평균 :: ", sum(rArr) / arrLen)

    # print(asclist[0])

    # for a in ascArr:
    #     print(a)


# if __name__ == "__name__":
main()
