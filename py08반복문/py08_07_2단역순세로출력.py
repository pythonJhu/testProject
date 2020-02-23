tmp = ""

for x in range(1, 10, 1):

    idx = 10 - x

    if idx == 1:
        tmp = tmp + "2 * %d = %2d" % (idx, 2*idx) + ". "
    else:
        tmp = tmp + "2 * %d = %2d" % (idx, 2*idx) + ",\n"

    pass

print(tmp)
