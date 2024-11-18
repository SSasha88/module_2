#first, second и third
first = input("first: ")
second = input("second: ")
third = input("third: ")
if first==second==third:
    print(3)
elif first==second or first==third:
    print(2)
else: print(0)