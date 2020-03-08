# 1. 파일 읽고 문자열에 텍스트 저장
# 2. 줄바꿈(\n) 을 제거한다. str.replace("\n", " ")
# 2. 딕셔너리 table 을 만든다.
# 3. 문자열을 split()  해서 array 리스트로 만든다.
# 4. 반복문을 사용하여 array 리스트를 루프 돌면서
#     1). 리스트 요소에서 첫글자를 추출한다. 선택 연산자 [] 사용
#         val = array[i][0] OR val = i[0]
#     2). 대문자와 소문자를 구분하지 않도록 소문자로 치환한다.
#         val  = val.lower()
#     3). 딕셔너리 table 에서 키값중에 val 있는지 확인한다.
#         ==>  table 에서 찾을때는 get() 메서드나 in 연산자를 사용한다.
#     3). 있으면 table[val] = table[val] + "-"
#          없으면 table[val] = "-"
# 5. 찾기가 끝나면 table 출력한다.

strTmp = """This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows."""

strTmp = strTmp.replace("\n", " ").replace("  ", " ")

# print("str ===> ", strTmp)

table = {}
arrList = strTmp.split(" ")
for i in range(0, len(arrList), 1):
    key = arrList[i][0]
    key = key.upper()
    tmp = table.get(key)

    if tmp == None:
        #table[key] = "-"
        table[key] = 1
    else:
        table[key] = table[key] + 1

# 출력.
for item in table.items():
    #print("items >>>> ", item[0], item[1])
    print(item[0], item[0]*item[1])  # item[0] 을 item[1] 번 반복하시오
    print()
