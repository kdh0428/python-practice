
Count_Of_Alphabats = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def F(N):
    result = 0
    global count
    global Count_Of_Alphabats
    for x in N[0:-1]:
        result += Count_Of_Alphabats.index(x)+1
    return result

f = open("./22.txt")
count = 1 
result = 0

for line in f:
    result += count*F(line) 
    count += 1
print result
