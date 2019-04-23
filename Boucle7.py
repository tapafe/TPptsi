def facto(n):
    S = 1
    for i in range(1,n):
        S *= int("F" + str(i) + "=" + str(S))

facto(60)