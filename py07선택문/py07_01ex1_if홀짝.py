# 정수를 입력을 받습니다.
# 입력 받은 문자열을 정수로 바꿉니다.
# i = int(input("정수 입력 :: "))

# # 문자열로 변환

# i = i%2
# print(i)

# if i == 0:
#     print("짝수 입니다.")

# if i == 1:
#     print("홀수 입니다.")


#######################################
# 방법1. 문자열을 사용하는 방법
# 방법2. 나머지를 사용하는 방법
#######################################

#######################################
# 방법1. 문자열을 사용하는 방법
#######################################
# 마지막 자리 숫자를 추출
i = input("정수 입력 :: ")

tLen = len(i)
print(tLen)

if tLen > 1:
    i = i[int(tLen) - 1]

print(i)

idx = 0
arr = ["1","3","5","7","9"]

print(len(arr))

while idx <= 5:
    print("idx === ", idx)

    # arr.index(idx)
    # if i == arr.index(idx):
    #     print("홀수 입니다.")
    # else:
    #     print("짝수 입니다.")
    
    idx += 1
    pass

print("종료")


# 숫자로 변환하기

# 짝수 확인

# 홀수 확인


#######################################
# 방법2. 나머지를 사용하는 방법
#######################################

# 짝수 조건

# 홀수 조건
