# py02_09ex1_Salary

# 변수 선언 : salary , deposit 정수 변수 선언
salary = 0
deposit = 0

# 숫자를 입력받고(이것은 문자열) salary 변수 에 저장하시오.
salary = input("월급을 입력하시오 :: ")

# 10년치 월급의 총합을 구하고 그 값을 deposit 에 저장.
print( type(salary) ) # <class, str>
deposit = 10 * 12 * int(salary)

# 10년 동안의 저축액: ?????  원 형태로 출력하시오.
print("10년동안 저축 금액 :: ", deposit, "원")