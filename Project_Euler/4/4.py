
def Erasto(N):
    for prime in N:
        for each in range(prime*2,max(N),prime):
            if(N.count(each)):
                N.remove(each)
    return N

result = 1
for prime in Erasto(range(2,21)):
    for scale in range(1,5):
        if(prime**scale < 20):
            print "%d * %d = %d" %( prime, scale,prime**scale)
            result *= prime
print result
