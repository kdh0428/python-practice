max_term = 0
for problem in xrange(2,1000000):
    term = 0
    temp_problem = problem
    while problem > 1:
        if problem % 2 == 0:
            problem /= 2
        else:
            problem = 3 * problem + 1
        term += 1 

    if max_term < term :
        answer = temp_problem
        max_term = term
print answer
