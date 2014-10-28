problem = 600851475143

def Erasto(N):
    for prime in N:
        for each in range(prime*2,max(N),prime):
            try:
                N.remove(each)
            except:
                pass
    return N

Erasto_list = Erasto(range(2,10000))

print max(filter(lambda x: problem % x ==0,Erasto_list))

