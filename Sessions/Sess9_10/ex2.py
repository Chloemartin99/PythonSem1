#write a function that tests if a number is odd or even, based on an extra parameter:
#f(number, odd=True)

def f(number, odd=True):
    if odd==True:
        if number % 2 == 1:
            return True
        else:
            return False
    else:
        if number % 2 == 0:
            return True
        else:
            return False

print(f(4, odd=False))

