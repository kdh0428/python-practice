abundantnum_list = []
sum_abundantnum_list = []
def divisor(N):
    cache_ = []
    for x in xrange(1,int(N/2)):
        if N/x in cache_ :
            return sum(cache_)-N
        if N%x == 0:
            cache_.append(x)
            cache_.append(N/x)


for number in xrange(12,28124):
    if number < divisor(number):
        abundantnum_list.append(number)


for abundantnum in abundantnum_list:
    for abundantnum2 in abundantnum_list:
            sum_abundantnum_list.append(abundantnum+abundantnum2)

print sum(range(1,28123))-sum(list(set(sum_abundantnum_list))) 
