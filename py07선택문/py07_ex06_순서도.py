in_data = input("문자열 입력 :: ")

#gbn = "F"

# while gbn == "F":
    
#     data_len = len(in_data)

#     if data_len < 3:
#         print("문자열이 짧습니다.", data_len)
#         in_data = input("문자열 입력 :: ")
#     else:
#         gbn = "T"
    
#     pass

data_len = len(in_data)

while data_len < 3:

    print("문자열이 짧습니다.", data_len)
    in_data = input("문자열 입력 :: ")
    data_len = len(in_data)
    pass

print("종료합니다.")