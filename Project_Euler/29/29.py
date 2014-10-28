#!/usr/bin/env python

answer_list = []

for a in xrange(2,101):
    for b in xrange(2,101):
        answer_list.append(a**b)

print len(list(set(answer_list)))
