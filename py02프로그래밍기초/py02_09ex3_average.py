value1 = input("첫번째 과목 점수를 입력하세요 : ")
value2 = input("두번째 과목 점수를 입력하세요 : ")

value1 = int(value1) # 문자열 value1 을 정수로 변환, 형변환
value2 = int(value2) # 문자열 value1 을 정수로 변환, 형변환

sum = value1 + value2
average = sum / 2

print(' ------------------ value1 = ', value1, ' value2 = ', value2, '-------------------- ')
if average >= 95:
    print('verry good')
else:
    print('just good')

print(' ------------------- average = ', average, '------------------- ')