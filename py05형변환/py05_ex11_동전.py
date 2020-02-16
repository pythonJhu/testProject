# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자. 
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다. 
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 
# 거스름돈을 계산하여서 동전으로 반환한다. 
pPrice = int(input("물건값을 입력하시오 : "))

cnt1000 = 0
cnt500 = 0
cnt100 = 0
cnt10 = 0
cnt1 = 0

totMoney = 0

while pPrice >  totMoney:
     
    cnt1000 =  int(input("1000원 지폐 : ")) 

    # 거스름돈(1000원 동전 개수)을 계산한다.
    totMoney = cnt1000 * 1000
    
    print("totMoney ::: ", totMoney)

    pass

#거스름돈
rTotPrice = totMoney - pPrice 
print("rTotPrice :: ", rTotPrice)

# 거스름돈(500원 동전 개수)을 계산한다. 
cnt500 = rTotPrice // 500

# 거스름돈(100원 동전 개수)을 계산한다. 
rTotPrice = rTotPrice % 500
cnt100 = rTotPrice // 100

rTotPrice = rTotPrice%100
cnt10 = rTotPrice // 10

cnt1 = rTotPrice%10

# 출력
print(" 500원  :: ", cnt500, " \n100원 :: ", cnt100, " \n10원 :: ", cnt10, " \n1원 :: ", cnt1)
