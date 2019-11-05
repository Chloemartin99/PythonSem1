#Determine the average of 4 random numbers
numbers = []

def giveAv(numbers):
    sum = 0
    for i in numbers:
        sum = sum +i

    return sum/len(numbers)

counter = 1

while (counter<=4):
    try:
        num = int(input('Enter a number: '))
        numbers.append(num)
        counter+=1

    except ValueError:
        print('You did not enter a valid number.')

print(numbers)

print(giveAv(numbers))