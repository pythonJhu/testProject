# 참석자에 맞추어서 치킨(1인당 1마리), 맥주(1인당 2캔), 
# 케익(1인당 4개)를 출력하는 프로그램을 작성해보자.


people = 0
chiken = 0
beer = 0
cake = 0

people = input("참석자 수를 입력하세요 : ")
people = int(people)

chiken = people * 1
beer = people * 2
cake = people * 4

print("people : ", people)
print("chiken : ", chiken)
print("beer : ", beer)
print("cake : ", cake)
