#Write a program that takes 2 numbers as input and prints the rounded up division result:
import math

print("Please enter two whole numbers separated by a comma: ")
num1, num2 = [int(i) for i in input().split(",")]
result = math.ceil(num1/num2) #ceiling function to round up even if the float decimal is <.5

print("The rounded up division of "+str(num1)+" by "+str(num2)+" is "+str(result))

#Another way of doing it:
#num1 = int(input("First num"))
#num2 = int(input("Second num"))
#result = int((num1/num2)+0.5)
#print("Result is "+str(result))
