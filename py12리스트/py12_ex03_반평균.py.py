
# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 3명이상
# 3. 학생 성적 입력 받기. 몇번 입력받아야 하는가?
# 4. list에 입력 받은 학생 성적을 추가한다.
# 5. 3번 학생의 성적을 100점으로 바꾸시오.
# 6. list에서 마지막 학생 삭제.
# 7. list에서 0번 값을 출력하시오.
# 8. 평균을 구하고 출력.

stdCnt = 0
while stdCnt < 3:
    strNum = input("학생수 입력 = ")

    try:
        stdCnt = int(strNum)
    except ValueError as ex:
        print(ex)

print("학생수 == ", stdCnt)

stdList = []
while stdCnt > len(stdList):
    strPoint = input("학생 성적 입력 = ")

    try:
        stdList.append(int(strPoint))
    except ValueError as ex:
        print(ex)

print("stdList1 ==== ", stdList)

stdList[2] = 100

# listCnt = len(stdList)
# print("listCnt == ", listCnt)
stdList.pop(len(stdList) - 1)
print("stdList2 ==== ", stdList)

print("stdList[0] == ", stdList[0])
svgPoint = sum(stdList) / len(stdList)
print("평균 ==> ", svgPoint)
