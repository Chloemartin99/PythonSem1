#Test if a given number is prime

num = int(input("Write a number"))
if num > 1:
    isprime = True
    for i in range(2, num//2):
        print(num)
        if(num % 1 == 0):
            print(num, "not prime")
            isprime = False
            break
    if isprime:
        print(num,"is prime")