num_1 = input("정수 입력")
num_2 = input("정수 입력")
num_3 = input("정수 입력")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    num_3 = int(num_3)

    # if num_1 > num_2:
        
    #     if num_1 > num_3:
    #         print(num_1)
    #     else:
    #         print(num_3)

    # else:
        
    #     if num_2 > num_3:
    #         print(num_2)
    #     else:
    #         print(num_3)

    if num_1 > num_2 and num_1 > num_3:
        print(num_1)
    elif  num_2 > num_3:
        print(num_2)
    else:
        print(num_3)

except ValueError:
    pass