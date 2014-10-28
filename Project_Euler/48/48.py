#!/usr/bin/env python
from multiprocessing import Pool

def F(x):
    return x**x
p = Pool(4)
print sum(p.map(F,xrange(1,1000+1)))
