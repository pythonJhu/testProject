

cnt = 0
totPoint = 0
while True:

    try:
        strPoint = input("성적을 입력 하시오:")
        intPoint = int(strPoint)

        # 입력값이 음수 이면 반복문 종료
        if intPoint < 0:
            break
        else:
            totPoint = totPoint + intPoint
            cnt += 1

        # 합계를 구함
    except ValueError:
        pass

print(totPoint,  cnt)
#svgPoint = int(totPoint / cnt)

#print(cnt, "과목 평균 ::: " + svgPoint)
