#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1_2_3_4_5_6_7_8_9_0
# 19 digits 100경
# 9자리 * 9자리
# 제곱 이므로 뒷자리가 0으로 끝나기 위해서는 0*0 즉 _900 단위를 낮출수 있음

# 1_2_3_4_5_6_7_8_9
# 8자리 * 8자리

from multiprocessing import Pool
min = 101010101
max = 138902663

def F(x):
    if int(str(x*x)[0::2]) == 123456789:
        return x*10
    return 0
Done =1 

p = Pool(4)

print filter(lambda x: x!=0,p.map(F,xrange(min,max,2)))
#for each in xrange(min,max):
#    if Done < (each/1.0-min)/(max/1.0-min)*100:
#        print "%d %% Done" % Done
#        Done += 1
#    if F(each):
#        print each*10

