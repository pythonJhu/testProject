
# # range(10)
# r1 = range(10)
# print("range(10)", r1)


# # range(0, 10, 1)
# r2 = range(0, 10, 1)
# print("range(0, 10, 1)", r2)


# # range(0, 10, 2)
# r3 = range(0, 10, 2)
# print("range(0, 10, 2)", r3)


# # range(0, 10, 1)
# r4 = range(10, 0, -1)
# print("range(10, 0, -1)", r4)

for x in range(2, 10, 1):
    print(x,"단")
    for y in range(1, 10, 1):
        gugu = x * y
        print(x," / ",y," == ", gugu)
        pass
    pass

# ch = input("문자열 입력 :: ")

# ch_len = len(ch)

# for i in range(0,ch_len,1):
#     print(i,ch[i])
#     pass

# for tCh in ch:
#     print(tCh)
#     pass