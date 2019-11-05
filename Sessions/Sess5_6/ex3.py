#Read an int number. Check if the number is a palindrome. (A palindrome number read backwards has the same value)
num = 678
temp = num
new_num = 0

while num>0:
    digit = num%10
    print(digit)
    new_num = new_num*10 + digit

    num = num//10

if new_num == temp:
    print('yes')

else:
    print('no')