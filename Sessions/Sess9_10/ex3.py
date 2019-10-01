#write a function that creates a list of random number of random numbers (a list of random numbers of random length)
import random
def rand():
    list_length = random.randint(5,50)
    my_list = []

    for i in range(list_length):
        my_list.append(random.randint(0,100))

    return(my_list)

print(rand())