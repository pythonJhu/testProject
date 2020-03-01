strTmp = input("정수 문자열 입력 = ")

arrlist = strTmp.split(" ")

numList = []
for i in arrlist:
    try:
        n = int(i)
        numList.append(n)
    except ValueError as ex:
        print(ex)

numList = sorted(numList)

print(numList)
