# 표준 입력 prompt을 이용하여 이름, 신장, 체중을 입력 받은 후 적정 평균 체중을 구하는  프로그램을 작성하시오.
#
# 적정 평균 체중 계산식 = (신장 - 100) * 0.9 ;
#
#
# 적정 평균 체중 오차는 ± 5 이며 방문자자 입력한 체중이 적정 체중일경우에는 "OOO님은 적정 체중입니다" 를, 아닐 경우에는 "OOO님은 적정 체중이 아닙니다" 를 출력하시오.
#
# 작성 과정.
# 변수 3개 만들고
# prompt를 이용하여 3번 값을 입력 받는다. 입력 받은 신장과 체중은 숫자로 형변환 한다.
# 표준 출력을 이용하여 결과를 화면에 출력한다.

myTall = float(input("신장 : "))
myWeight = float(input("몸무게 : "))

avgWeight = float( (myTall - 100) * 0.9 )
print("적정 평균 체중 :: ", avgWeight)

if avgWeight-5 < myWeight and myWeight < avgWeight+5 :
    print("jhu님은 적정 체중입니다")
else:
    if myWeight > avgWeight+5 :
        print("살빼!!")
    elif myWeight < avgWeight-5 :
        print("많이먹어!!")
    pass
