
# 2단의 구구단을 가로 출력하는 프로그램을 만드시오. 끝날 때는 마침표를 붙인다.
# 힌트. 출력할 문자열을 변수에 저장하고 마지막 한번만 변수값을 print()를 사용하야 출력해야 한다.

tmp = ""

for x in range(1,10,1):

    #print("2 * %s = %2s" % (x, 2*x))
    #print("2 * %d = %2d" % (x, 2*x))

    if x == 9:
        tmp = tmp + "2 * %d = %2d" % (x, 2*x) + ". "
    else:
        tmp = tmp + "2 * %d = %2d" % (x, 2*x) + ",  "

    pass

print(tmp)