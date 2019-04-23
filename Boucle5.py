def fibo(n):
    a = 1
    b = 1
    for i in range(n):
        a,b = b,a+b
        print ("F" + str(i) + "=" + str(a))
    
fibo(16)