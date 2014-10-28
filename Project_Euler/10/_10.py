import math
from multiprocessing import Pool

def isprime(x):
    for each in xrange(2,int(math.ceil(math.sqrt(x)))+1):
        if x%each == 0:
            return 0
    else:
        return x


p = Pool(4)

print 2+sum(p.map(isprime, xrange(3,2000000,2)))

