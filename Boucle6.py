def harmo(n):
    S = 0
    for k in range(1,n):
        S += 1/k
        print ("F" + str(k) + "=" + str(S))
    
harmo(1000)