def Erasto(N):
    for prime in N:
        for each in xrange(prime*2,max(N),prime):
            if(N.count(each)):
                N.remove(each)
    return N

sum(Erasto(range(2,2000000)))
