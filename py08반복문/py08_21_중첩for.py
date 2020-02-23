# 중첩 for문

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
x = 0
y = 0

# for x in range(0, 10, 1):
#     for y in range(0, 10, 1):
#         print("*", end="")
#     print()

# print()

# for x in range(0, 10, 1):
#     for y in range(0, x, 1):
#         # print(x, y)
#         print("*", end="")
#     print()

# print()

# for x in range(0, 10, 1):
#     for y in range(1, 11, 1):
#         if x >= y:
#             print(" ", end="")
#         else:
#             print("*", end="")

#     print()

# print()

for y in range(0, 9, 1):
    for x in range(0, 9, 1):
        if y <= 4:
            print(y, x)
            # if x < y:
            #     print(" ", end="")
            # else:
            #     print("*", end="")
        pass
    print()
    pass
