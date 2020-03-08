# 1. 문자여을 split() 해서 array 리스트로 만든다.
# 2. 반복문을 사용하여 array 리스트를 루프를 돌면서 딕셔너리 table에 찾는다
# 3. 찾았다면 바꾼다. replace()
# 4. 출력한다. 문자열 join() 메서드를 사용하는 것으로 작성한다


def get_Sentence(s):
    value = table.get(s)
    return value


table = {
    "B4": "Before", "TX": "Thanks", "BBL": "Be Back Later", "BCNU": "Be Seeing You", "HAND": "Have A Nice Day", "": ""
}


def main():

    strTmp = input("축약어를 입력하시오 : ")

    strList = strTmp.split(" ")
    print("strList :: ", strList)

    for x in strList:
        v = get_Sentence(x)

        if v == None:
            pass
        else:
            strTmp = strTmp.replace(x, v)

    print("End ::: ", strTmp)


if __name__ == "__main__":
    main()
