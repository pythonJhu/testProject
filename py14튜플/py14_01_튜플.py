address = input("이메일 주소를 입력하시오 : ")

t = address.find("@")

if t != -1:
    (id, domain) = address.split('@')
    print(address)
    print('            ' + id)
    print('            ' + domain)

    arr = address.split('@')
