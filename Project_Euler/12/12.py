import math
def isprime(x):
    for each in xrange(2,int(math.ceil(math.sqrt(x)))+1):
        if x%each == 0:
            return 0
    else:
        return x

def TriangleNum_Generator():
    Step = 1
    Num = 0
    while True:
        Num += Step
        yield Num
        Step += 1

prime_list = [2]+filter(lambda x: x!=0,map(isprime, xrange(3,500,2)))



for num in TriangleNum_Generator():
    result = 1
    result_num = num
    for prime in prime_list:
        multiple_time = 1
        if num == 1:
            break
        while num >1 :
            if num%prime == 0:
                multiple_time += 1
                num /= prime
            else:
                break
        result *= multiple_time
        
    if result > 500:
        print "Triangle : %d a number of Divisor : %d" % (result_num,result)
        break
