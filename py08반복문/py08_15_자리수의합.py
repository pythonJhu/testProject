strTmp = input("+수식 입력 :: ")

strLen = len(strTmp)

i = 0
sumNum = 0
strNum = ""
intNum = 0

for i in range(i, strLen, 1):

    try:

        if "1" <= strTmp[i] and strTmp[i] <= "9":
            strNum = strNum + strTmp[i]
            print(i, " :::: ", strTmp[i], strNum)
        else:
            intNum = int(strNum)
            sumNum = sumNum + intNum
            print("sumNum ::: ", sumNum)

            strNum = ""
            intNum = 0

    except ValueError:
        pass

print(strTmp, sumNum)
