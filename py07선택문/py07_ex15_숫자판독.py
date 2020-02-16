# 문자열을 입력 받고 숫자인지 문자인지 판별하는 프로그램을 작성하시오.

ch = input("입력 :: ")

# 영문 아스키 코드 98 ~ 122
if ( "a" <= ch and ch <= "z") or ( "A" <= ch and ch <= "Z") :
    print("영문 입니다")
else:
    print("숫자 입니다")