import itertools
count =1
for x in itertools.permutations(range(0,10)):
    if count == 1000000:
        result = reduce(lambda result,d: result*10 + d,x)
        break
    count += 1

print result
