# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고    
# 90점 이상이면 A,    90이상이고 100이하이면
# 80점 이상이면 B,    80이상이고 90미만이면
# 70점 이상이면 C,    70이상이고 80미만이면
# 60점 이상이면 D,    60이상이고 70미만이면
# 나머지는 F                60미만이면

grade = input("정수입력 :: ")
grade = int(grade)

if ( 90 <= grade and grade <= 100 ):
    print("A")
elif ( 80<= grade and grade < 90 ):
    print("B")
elif ( 70<= grade and grade < 80 ):
    print("C")
elif ( 60<= grade and grade < 70 ):
    print("D")        
else:
    print("F")

# if ( 90 <= grade ):
#     print("A")
# elif ( 80<= grade ):
#     print("B")
# elif ( 70<= grade ):
#     print("C")
# elif ( 60<= grade ):
#     print("D")        
# else:
#     print("F")
