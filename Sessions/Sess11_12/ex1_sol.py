#Determine the max out of 4 given numbers
def f (list_numbers):
    m = list_numbers[0]
    for i in list_numbers:
        if i>m :
            m = i

    return m
number_list = []
import random
for i in range(4):
    number_list.append(random.randint(-1000, 1000))
a = f (number_list)
print(a)
print (number_list)