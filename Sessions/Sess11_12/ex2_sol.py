#Determine the average of 4 random numbers
def avg(list_numbers):
    sum = 0
    for i in list_numbers:
        sum = sum + i
    average = sum/len(list_numbers)
    return average

'This is just a function'
'Ask the user for 4 numbers'

i = 0
numbers_list = []
while (i<4):
    try:
        n = input('give me a number')
        n = int(n)
        numbers_list.append(n)
        i = i + 1
    except ValueError:
        print('Please enter a number')
print(avg(numbers_list))