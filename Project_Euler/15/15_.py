
def paths (grid):
    #pretty readable recursive solution. total path options is last item in list.
    lst = []
    a = [1]
    if grid == 2 : return [1, 3, 6]
    #grid==1 skipped .. solution would be [1, 2]
    else :
        lst = paths(grid-1)
        for i in range(1,len(lst)):
            a.append(a[-1]+lst)
        a.append(a[-1]*2)    
        return a


print paths(20)
