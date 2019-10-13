#Determine the first and second largest numbers of 4 random numbers
import random
numbers = []

def giveMax(numbers):

    for j in range(2):
        try:
            temp = numbers[0]
            for i in numbers:
                if i>temp:
                    temp = i

            print('max '+str(j+1)+': '+str(temp))

            while temp in numbers: #In case that the largest number is twice in the list, avoid the second largest number being equal to the largest number
                numbers.remove(temp)
        except IndexError:  #In case all numbers in the list are equal, for which they would all be removed
            print('No second largest number.')

for i in range(4):
    numbers.append(random.randint(-100, 100))
print('From the following numbers: ', numbers)
giveMax(numbers)