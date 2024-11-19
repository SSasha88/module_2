print('вариант 1')
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
print('вариант 2')
my_list1 = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
f = 0
while f < len(my_list1):
    if my_list1[f] > 0:
        print(my_list1[f])
        f += 1
    elif my_list1[f] == 0:
        f += 1
        continue
    else:
        break

