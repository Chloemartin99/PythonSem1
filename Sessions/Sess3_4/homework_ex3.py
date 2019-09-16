#Write a program that takes the radius of circle as input and prints the surface of the circle
import math

print("Please enter the radius of the circle: ")
radius = int(input())
surface_area = round((math.pi*(radius**2)), 2)

print("The surface area of the circle is "+str(surface_area)+" (rounded to two decimal places)")