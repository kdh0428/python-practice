
cache_ = [None] * 10000
def Fibo(N):
    if cache_[N]: return cache_[N]
    if N < 2:
        if N == 1:
            return 1
        return 0
    else:
        rst = Fibo(N-1) + Fibo(N-2)
        cache_[N] = rst
        return rst

N = 0
while len(list(str(Fibo(N)))) < 1000:
    N += 1

print N
