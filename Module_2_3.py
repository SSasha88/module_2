my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
c = len(my_list)
# b = my_list
while c > 0:
    for x in my_list:
        if x > 0:
            print(x)
        if x < 0:
            break
        continue
    break
