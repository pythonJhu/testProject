# swap 이란 ? 변수의 값을 바꾸는 코딩 기법

# 1. 외팔이 방법. 모든 프로그래밍에서 가능
x = 2
y = 3

strTmp = "0.  x == %s , y == %s" % (x, y)
print(strTmp)

tmp = x
x = y
y = tmp

strTmp = "1.  x == %s , y == %s" % (x, y)
print(strTmp)

# 2. 튜플을 사용하는 방법. 파이썬에서만 가능
(x, y) = (y, x)
strTmp = "2.  x == %s , y == %s" % (x, y)
print(strTmp)
