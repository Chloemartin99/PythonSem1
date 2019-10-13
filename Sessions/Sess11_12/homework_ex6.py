#Check if all letters in a word are tripled (they should be beside each other)

str = input('Enter string to be validated: ')

if str[::3] == str[1::3] == str[2::3]:
    check = True

else:
    check = False

print(check)