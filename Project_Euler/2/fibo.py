#!/usr/bin/env python

_cache = [None] * 150
def fibo(n):
    global _cache
    if _cache[n]: return _cache[n]
    if n < 2:
        _cache[0] = 0;
        _cache[1] = 1;
        return 1
    else:
        rst = fibo(n-2) + fibo(n-1)
        _cache[n] = rst
        return rst

print fibo(98)
