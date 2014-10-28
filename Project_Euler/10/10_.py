#!/usr/bin/env python 
#-*-coding: utf-8 -*-

from multiprocessing import Pool
import math
cache = [2]
step = 100000

def is_prime_early(n):
    global cache
    for each in xrange(3,n,2):
        if n%each == 0:
            return 0
    return n

def is_prime(n):
    global cache
    for each in xrange(max(cache),int(math.ceil(math.sqrt(n),2))):
        if n%each == 0:
            return 0
    return n

# Stage 1
total = 0
cache += map(is_prime_early, range(3,1000,2))
while 0 in cache:
    cache.remove(0)

for i in xrange(3,200000, step):
    rst = []
    for x in xrange(i,i+step,2):
        for y in cache:
            if x%y == 0:
                break
        else:
            rst.append(x)
    print 'Reduced,', len(rst)

    # Stage 2
    p = Pool(4)
    cache += p.map(is_prime, rst)
    while 0 in cache:
        cache.remove(0)
print sum(cache)
