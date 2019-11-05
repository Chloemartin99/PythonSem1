#Determine the max out of 4 given numbers

import random
numbers = []

def giveMax(numbers):
    max = numbers[0]

    for i in numbers:
        if i>max:
            max = i

    return max

for i in range(4):
    numbers.append(random.randint(-10, 10))

print(giveMax(numbers))

print(numbers)



