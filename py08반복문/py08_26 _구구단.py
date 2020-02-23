# stDan = input("시작 : ")
# edDan = input("종료 : ")

# stDan = int(stDan)
# edDan = int(edDan)


while True:

    try:
        stDan = input("시작 : ")
        edDan = input("종료 : ")

        if ("0" <= stDan and stDan <= "9") and ("0" <= edDan and edDan <= "9"):
            stDan = int(stDan)
            edDan = int(edDan)

            tmpDan = 0
            if stDan > edDan:
                tmpDan = stDan
                stDan = edDan
                edDan = tmpDan

            break

    except ValueError:
        break

    pass

print(stDan, edDan)
guguStr = ""

if stDan > 0 and edDan > 0:
    for y in range(stDan, edDan+1, 1):
        for x in range(0, 10, 1):
            # %2s, %3s 는 자리수를 맞추기 위해서
            guguStr = "%2s * %s = %3s" % (y, x,  y * x)
            print(guguStr, end=" ")
        print()

print("종료")
