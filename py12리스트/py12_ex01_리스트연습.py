############################
# 리스트에 담을 수 있는 것은? => 다 할수 있음
# 리스트 선언 => [], list()
# 리스트 대입 => =
# 리스트 추가 => .append() ,insert()
# 리스트 읽기 => [방번호]
# 리스트 수정 => [방번호] = 값
# 리스트 삭제 => .pop() , del list[0], .remove()
# 리스트 정렬 => sorted()
# 리스트 정렬 => .find() + 반복문, .rfind() + 반복문
# 리스트 합치지 => +, .extend()
# 리스트 길이 => len()
# 리스트에 저장된 함수 실행하기
############################
pos = 0
value = ""

#  List 선언
arrlist = []

#  C: 추가. 검색: "파이썬 리스트 추가"
#  MILK, BREAD, BUTTER 순으로 추가
#
arrlist.append("MILK")
arrlist.append("BREAD")
arrlist.append("BUTTER")
print(arrlist)

#  APPLE 삽입. 검색: "파이썬 리스트 삽입"
#  특정 위치에 추가하기
#  "BREAD" 앞에 "APPLE" 삽입
#  "BREAD" 가 들어있는 방번호 찾기
idx = arrlist.index("BREAD")
print("index = ", idx)
arrlist.insert(idx, "APPLE")
print(arrlist)

#  R: 읽기
#  BUTTER 값을 출력하시오.
#  "BUTTER" 가 들어있는 방번호 찾기
#
idx = arrlist.index("BUTTER")
print(idx, " == ", arrlist[idx])

#  U: 수정. 검색: "파이썬 리스트 수정"
#  "BREAD" 를 "GRAPE"로 변경
#  "BREAD" 가 들어있는 방번호 찾기
#
print(arrlist)
idx = arrlist.index("BREAD")
arrlist[idx] = "GRAPE"
print(arrlist)

#  D: 인덱스로 삭제. 검색: "파이썬 리스트 삭제"
#  인덱스를 이용하여 GRAPE 를 삭제
#
idx = arrlist.index("GRAPE")
arrlist.pop(idx)
print(arrlist)

#  D: 값으로 찾아서 삭제. 검색: "파이썬 리스트 값으로 삭제"
#  값으로 MILK를 찾아서 삭제하시오
#


#  P: 리스트를 for문으로 출력.
#  검색: "파이썬 리스트 for 출력"
#  검색: "파이썬 리스트 크기"
#
for i in arrlist:
    print(i)

for i in range(0, len(arrlist), 1):
    print("for == ", arrlist[i])

n = 0
while n < len(arrlist):
    print("while == ", arrlist[n])
    n += 1

#  P: 리스트를 for-each문으로 출력.
#


#  테스트용 데이터 생성을 위한 코드. 수정하지 마시오.
# for i in range(4):
#     list.append("APPLE")
#     list.append("BANNA")


#  S: 검색: "파이썬 리스트 검색
#  첫번째 APPLE을 찾으시오.
idx = arrlist.index("APPLE")
print("APPLE == ", idx)
arrlist.insert(idx, "MANGO")

#  S: 오름차순 정렬. 검색: "파이썬 리스트 오름차순 정렬"
print(arrlist)
arrlist = sorted(arrlist)
print(arrlist)
arrlist.append("APPLEMANGO")
print(arrlist)

#  S: 내림차순 정렬. 검색: "파이썬 리스트 내림차순 정렬"
arrlist.reverse()
print("after reverse == ", arrlist)

#  검색2. APPLE 이 몇개 있나요?


#  변환된 배열을 for 문으로 출력.
# for x in arrlist:
#     print(x)

#  list의 모든 값을 while문을 사용하여 삭제하시오
# print("remove before == ", arrlist)
# arrlist.remove()
# print("remove after == ", arrlist)


# arrlist.append("MILK")
# arrlist.append("BREAD")
# arrlist.append("BUTTER")
# print(arrlist)


while True:

    if len(arrlist) == 0:
        break
    else:
        arrlist.pop(0)


print("after while == ", arrlist)


# print("while pop after == ", arrlist)
