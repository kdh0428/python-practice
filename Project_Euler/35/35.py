#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
def isprime(x):
    for each in xrange(2,int(math.ceil(math.sqrt(x)))+1):
        if x%each == 0:
            return 0
    else:
        return x

def circular_num(x):
    str_x = str(x)
    for count in xrange(0,len(str_x)+1):
        if isprime(int(str_x)) == 0:
            break
        str_x = str_x[1:]+str_x[0]
    else:
        return x
    return 0

print len(filter(lambda x:x!=0,map(circular_num,filter(lambda x:x!=0,map(isprime,xrange(3,1000000,2))))))+1

