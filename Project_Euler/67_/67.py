problem = open("triangle.txt","r")
problem_list = []
while True:
    line = problem.readline()
    if not line:
        break
    problem_list.append(map(lambda x: int(x),line.split()))

while len(problem_list) > 1:
    last_row = problem_list.pop(-1)
    min_index = 0
    max_index = 2
    for index in xrange(0,len(problem_list[-1])):
        problem_list[-1][index] += max(last_row[min_index:max_index])
        max_index += 1
        min_index += 1

print problem_list
