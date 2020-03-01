
# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"


#################################
# 문자열 함수 / 문자열 메서드
#################################

# 문자열 길이: len().  prov의 길이를 출력하시오
strLen = len(prov)
print(strLen)

# 첫번째 b 문자를 찾고 위치를 출력하시오.
strIdx = prov.find("b")
print(strIdx)

# 문자열에 "Dog"가 있으면 "Dog있음"을 없으면 "Dog없음" 을 출력하시오
# "Dog 있음"
findDog = prov.find("Dog")
print(findDog)

if findDog != -1:
    provChg = prov.replace("Dog", "Cat")
    print(provChg)
else:
    print("Dog없음")

# 문자열 치환: replace()
# prov 문자열에 Dog가 들어 있으면 Cat으로 바꾸어 출력하고
# 아니면 prov 출력하시오.
# provChg = prov.replace("Dog", "Cat")
# print(provChg)

# 문자열 prov 를 공백을 기준으로 자르고 그 결과를 출력하시오.
provList = prov.split(" ")

print(provList)

# listLen = len(provList)
# for i in range(0, listLen, 1):
#     strTmp = "%s : %s" % (i, provList[i])
#     print(strTmp)

for i in provList:
    print(i, end=",")
