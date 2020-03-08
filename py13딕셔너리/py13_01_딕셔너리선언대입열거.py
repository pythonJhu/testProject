# 딕셔너리의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle

# 딕셔너리 선언하기
dictionary = {
    "name": "7D 망고", "type": "당", "ingredient": ["망고", "설탕", "소금", "치자"], "origin": "필리핀"
}

# 요소 추가 전에 내용을 출력해봅니다.
print(type(dictionary), dictionary)
print("name : ", dictionary["name"])
print("type : ", dictionary["type"])
print("ingredient : ", dictionary["ingredient"])
print("origin : ", dictionary["origin"])

# 딕셔너리 추가
dictionary["head"] = "머리"
dictionary["body"] = "몸"


# 선택 연사자로 딕셔너리 읽기
print("head : ", dictionary["head"])
print("body : ", dictionary["body"])

print("body get : ", dictionary.get("body"))

# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# dictionary["존재하지 않는 키"] # KeyError
try:
    dictionary["존재하지 않는 키"]
except KeyError as ex:
    print(ex)


# 딕셔너리 수정
# name 값을 "8D 망고" 로 수정 하시오
print("name bf : ", dictionary["name"])
dictionary["name"] = "8D 망고"
print("name  af : ", dictionary["name"])

# 딕셔너리 삭제.
# 1. 연산자 방식 => del      비추천
# 2. 메서드 방식 => .pop() 추 천
# name 키를 삭제
# type 키를 삭제
print("삭제 전 :: ", dictionary)
dictionary.pop("name")
del dictionary["type"]
print("삭제 후 :: ", dictionary)

# 존재하지 않는 키에 접근하면 에러 발생. try ~ except 사용
# 딕셔너리 키 존재 여부 확인 =>


# value = dictionary["존재하지 않는 키"]  # KeyError

# 방법1. .get() 메서드 사용
# 키가 존재하지 않는 경우의 확인 방법 :  None 사용
value = dictionary.get("존재하지 않는 키")  # value 값이 None 이면 키가 없다는 의미

if value == None:
    print("키 없다")
else:
    print("키 있다")
    print(value)

# 방법2. in
if "존재하지 않는 키" in dictionary:
    print("키값이 존재한다.")
    print(dictionary["존재하지 않는 키"])
else:
    print("키가 존재하지 않는다.")

print()

# 출력합니다.

# S : 정렬. 딕셔너리는 정령하는 방법이 없다
# 단, key 값만 정렬하는 것은 가능하다, value 값만 정렬하는 것은 가능하다.

# S : 검색. 특별한 방법은 없다.
# 선택연산자를 사용하면 바로 검색 되기 때문

################################
# 딕셔너리 열거
################################

# key 만 열거
for key in dictionary.keys():
    print("key >>> ", key)

# value 만 열거
for value in dictionary.values():
    print("value >>> ", value)

# key, value를 쌍으로 열거
for item in dictionary.items():
    print("item >>> ", item)
