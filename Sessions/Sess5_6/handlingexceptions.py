try:
    num = input("Give me a number")
    num = int(num)
    num2 = input("Give me another number")
    num2 = int(num2)
    result = num / num2
    print("The division result is"+str(result))

except ValueError:
    print("Give me a proper number")

except ZeroDivisionError:
    print("Second num cannot be zero")

except:
    print("Not valid.")