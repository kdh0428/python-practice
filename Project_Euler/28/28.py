#!/usr/bin/env python




limit = 1001 
problem = []

problem.append(range(limit*(limit-1)+1,limit*limit+1))

for x in xrange(0,limit-1):
    problem.append([None]*limit)


count = limit*(limit-1)+1
x,y = 0,0
point_x,point_y = 1,1


for t in xrange(limit-1,0,-1):
    for s in xrange(0,t):
        problem[y][x] = count
        y += point_y
        count -= 1
    for w in xrange(0,t):
        problem[y][x] = count
        x += point_x
        count -= 1
    point_x = -(point_x)
    point_y = -(point_y)

problem[y][x] = count

result = 0
for position in xrange(0,limit/2):
    result += problem[position][position]
    result += problem[limit-1-position][position]
    result += problem[position][limit-1-position]
    result += problem[limit-1-position][limit-1-position]

print result+count
