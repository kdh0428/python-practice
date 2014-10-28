Number_list = ['one','two','three','four','five','six','seven','eight','nine']
Number_list2 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
Number_list4 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

Word_list = []

for number in xrange(1,1001):
    if number == 1000:
        Word_list.append("onethousand")
    elif int(number/100) > 0:
        Word_list.append(Number_list[number/100-1])
        Word_list.append('hundred')
        if number%100 != 0:
            Word_list.append('and')
    
    if number%100 >= 20:
        Word_list.append(Number_list2[number%100/10-2])
    
    if number%100 < 20 and number%100 >= 10:
        Word_list.append(Number_list4[number%100-10])
    
    elif number%10 >0:
        Word_list.append(Number_list[number%10-1])
        


print len(''.join(Word_list))

