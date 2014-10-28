def F(N):
    cache_ = []
    for x in xrange(1,int(N/2)):
        if N/x in cache_ :
            return sum(cache_)-N
        if N%x == 0:
            cache_.append(x)
            cache_.append(N/x)

answer = 0

for x in xrange(2,10000):
    amicable_N = F(x)
    if amicable_N:
        if x != amicable_N:
            if x == F(amicable_N):
                answer += x


print answer
