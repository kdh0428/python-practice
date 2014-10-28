palindrome_list = []
for first in range(100,1000):
    for second in range(100,1000):
        if str(second*first) == str(second*first)[::-1]:
            palindrome_list.append(second*first)

print max(palindrome_list)
