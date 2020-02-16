#w = float(input("가로 길이 입력 : "))
#h = float(input("세로 길이 입력 : "))

#w = int(w)
#h = int(h)

w = input("가로 길이 입력 : ")
h = input("세로 길이 입력 : ")

try:

    w = float(w)
    h = float(h)

    area = w * h
    perimeter = 2 * (w+h)

except ValueError :
    pass

print("사각형의 넓이 :: ", area)
print("사각형읜 둘래 :: ", perimeter)