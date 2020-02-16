# 0부터 9까지의 합계를 구하시오
tSum = 0

# for x in range(0,10,1):
#     tSum += 1    
#     pass

# monSalary = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

# for salary in monSalary:
#     tSum = tSum + salary
#     pass


for i in range(0,102,2):
    tSum = tSum + i
    print(i, tSum)
    pass

print(tSum)
