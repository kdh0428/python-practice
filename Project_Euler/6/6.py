def Erasto(N):
    count = 0
    for prime in N:
        count+=1
        if(count>10000):
            return prime
        for each in range(prime*2,max(N),prime):
            if(N.count(each)):
                N.remove(each)
    return N

print Erasto(range(2,120000))
