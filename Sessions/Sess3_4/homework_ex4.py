#Write a program that behaves like a pocket calculator that can do: (+,-,*,/) of 2 numbers.
import sys
print("Enter calculation: ")
try:
    result = eval(input())
except ZeroDivisionError:
    print("Invalid calculation. Program ends.")
    sys.exit()

print("= "+str(result))