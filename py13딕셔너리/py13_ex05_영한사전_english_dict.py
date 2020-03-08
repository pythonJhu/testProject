# 영한사전 만들기


def getEnglish(dic, nm):

    value = dic.get(nm)
    return value


def main():
    dictionary = {
        "사과": "apple", "배": "ship", "어렵다": "difficult", "영어": "English", "엄마": "mother", "아빠": "father", "안녕하세요": "Hello", "안녕": "Hi"
    }

    while True:
        kor = input("검색어 입력 : ")

        eng = getEnglish(dictionary, kor)

        if eng == None:
            pass
        else:
            tmp = "%s ===> %s" % (kor, eng)
            print(tmp)
            break


if __name__ == "__main__":
    main()
