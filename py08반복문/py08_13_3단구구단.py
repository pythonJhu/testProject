guNum = int(input("구구단 몇단? :: "))

i = 1
guguDan = 0

while i < 10:
    guguDan = guNum * i
    strTmp = "%s 단 :: %s * %s = %s" % (guNum, guNum, i, guguDan)
    print(strTmp)
    i += 1
