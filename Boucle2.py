def heron(n, u0):
    u = u0
    for n in range(n):
        u=1/2 * (u + 2/u)
        print(u)
    
heron(5, 5)
        