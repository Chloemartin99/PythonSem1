#Test if a given number is prime

while True:
    try:
        num = int(input('Enter an integer number: '))
        prime = True

        if num<=1:
            prime = False

        for i in range(2, num):
            if num%i==0:
                prime = False
                break

        if prime==True:
            print('Prime number.')

        else:
            print('Not prime.')

        break

    except ValueError:
        print('You did not enter a valid number.')