#!/usr/bin/env python
answer = []
def Fact(N):
    if N < 2 :
        return 1
    return N*Fact(N-1)

for number in xrange(3,100000):
    if number == reduce(int.__add__,map(lambda x: Fact(int(x)),list(str(number)))):
        answer.append(number)

print sum(answer)
        
