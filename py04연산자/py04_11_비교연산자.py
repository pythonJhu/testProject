flag = True
print(flag)

flag = (2 > 3)
print("flag => ", flag)

print("True => ", True)
print("False => ", False)
print("10 == 100 : ", 10 == 100)
print("10 != 100 : ", 10 != 100)
print("10 < 100 : ", 10 < 100)
print("10 > 100 : ", 10 > 100)
print("10 <= 100 : ", 10 <= 100)
print("10 >= 100 : ", 10 >= 100)

print("가방 == 가방 : ", "가방" == "가방")
print("가방 != 하마 : ", "가방" != "하마")
print("가방 < 하마 : ", "가방" < "하마") # 문자 비교연산자의 판별 기준은 사전으로 이해
print("가방 > 하마 : ", "가방" > "하마") # 문자도 비교 연산이 가능하다.

x = 25
print("10 < x < 30 :: ", 10 < x < 30 )
print("10 < x < 30 :: ", 10 < x and x < 30 )

print("40 < x < 60 :: ", 40 < x < 60 )
print("40 < x < 60 :: ", 40 < x and x < 60 )
