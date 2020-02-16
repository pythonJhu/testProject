# 문자열 포매팅
#"I eat %d apples." % 3
#'I eat 3 apples.'
strTmp = "I eat %d apples." % 3
print(strTmp)

number = 10
day = "three"
#"I ate %d apples. so I was sick for %s days." % (number, day)
# 'I ate 10 apples. so I was sick for three days.'
print("I ate %d apples. so I was sick for %s days." % (number, day))

# 정렬과 공백
print("%10s" % "hi")  # '        hi'
print("%-10sjane." % 'hi')  # 'hi        jane.'

# 소수점 표현
print("%0.4f" % 3.42134234)  # '3.4213'
print("%10.4f" % 3.42134234)  # '    3.4213'