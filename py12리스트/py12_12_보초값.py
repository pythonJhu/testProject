
def entPoint():

    plist = []
    while True:

        try:
            strPoint = input("성적을 입력 하시오:")
            intPoint = int(strPoint)

            # 입력값이 음수 이면 반복문 종료
            if intPoint < 0:
                return plist
            else:
                plist.append(intPoint)

            # 합계를 구함
        except ValueError as ex:
            print("ex ::: ", ex)


def main():
    rlist = entPoint()
    print("최고 = ", max(rlist))
    print("최저 = ", min(rlist))
    print("과목수 = ", len(rlist))
    print("총점 = ", sum(rlist))
    svgPoint = "평균 = %0.2f" % (sum(rlist) / len(rlist))
    print(svgPoint)
    print("평균(round) = ", round(sum(rlist) / len(rlist)))


if __name__ == "__main__":
    main()
