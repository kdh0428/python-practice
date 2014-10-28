def Fact(N):
    if N < 2 :
        return 1
    return N*Fact(N-1)

print reduce(int.__add__,map(lambda x: int(x),list(str(Fact(100)))))
