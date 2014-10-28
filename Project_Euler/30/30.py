#!/usr/bin/env python
answer = []
for x in xrange(2,250000):
    result = 0
    for power in list(str(x)):
        result += int(power)**5

    if result == x:
        answer.append(x)

print sum(answer)
