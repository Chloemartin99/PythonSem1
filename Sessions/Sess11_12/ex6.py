#Check if all letters in a word are doubled (beside each other should have a pair)
str = input('Enter a string to be checked: ')

if str[::2] == str[1::2]:
    check = True

else:
    check = False

print(check)