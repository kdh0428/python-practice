def symmetry(list):
    temp_list = list
    for object in list[len(list)-2+len(list)%2::-1]:
        temp_list.append(object)
    return temp_list
