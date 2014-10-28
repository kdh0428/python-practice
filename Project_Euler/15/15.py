#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import symmetry
try:
    line = abs(int(sys.argv[1]))
except: 
    print "Usage: python 15.py <Line_Number> or ./15.py <Line_Number>"
    exit(0)


def Pascal_Triangle(N):
    if N<3:
        if N == 1:
            return [1]
        if N == 2:
            return [1,2,1]

    else:
        Pascal_Triangle_list = [range(0,N)]
        Pascal_Triangle_list[0][1] = 0
        N_Pascal_Triangle = [1]
        for time in xrange(0,N):
            temp_list = [0]
            for each in Pascal_Triangle_list[-1][2:]:
                temp_list.append(max(temp_list)+each)

            Pascal_Triangle_list.append(temp_list)

        for position in xrange(0,int(N/2)):
            if N-1+(-2*position):
                N_Pascal_Triangle.append(max(N_Pascal_Triangle)+Pascal_Triangle_list[position][N-1+(-2*position)])


        return N_Pascal_Triangle

print symmetry.symmetry(Pascal_Triangle(line))
