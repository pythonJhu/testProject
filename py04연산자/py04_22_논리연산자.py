x = 3
y = 4

r = ( (x == 3) and (y == 3))
#r2 = ( (x == 3) && (y == 3))
print(" ( (x == 3) && (y == 3)) ::: ", r)
#print("( (x == 3) && (y == 3)) : ", r2)

r = ( (x == 3) and (y != 3))
print(" ( (x == 3) && (y != 3)) ::: ", r)

r = ( (x == 3) or (y == 3))
print(" ( (x == 3) || (y == 3)) ::: ", r)

r = ( (x == 3) or (y == 4))
print(" ( (x == 3) || (y == 4)) :::: ", r)

r = ( (x != 3) or (y == 4))
print(" ( (x != 3) || (y == 4)) :::: ", r)

r = ( (x != 3) or (y != 4))
print(" ( (x != 3) || (y != 4)) :::: ", r)

# 변수 선언과 초기화
x = 3
y = 4
print((x == y) and (x != y)) # false and true = false
print((x > y) or (x < y)) # false or true = true
print((x >= y) or (x <= y)) # false or true = true
print(((x == y) and (x != y)) or (x < y)) # false and true or true = true