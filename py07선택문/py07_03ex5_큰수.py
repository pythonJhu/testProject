x = input("x ::")
y = input("y ::")

gbn = "F"

while gbn == "F":

    try:
        x = input("x ::")
        y = input("y ::")

        x = int(x)
        y = int(y)

        gbn = "T"
    except ValueError:
        pass

    pass

if x > y:
    print("큰수")
elif x == y:
    print("같다")
else:
    print(y)
