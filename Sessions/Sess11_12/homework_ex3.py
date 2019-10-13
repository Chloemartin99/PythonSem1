# read the value for the sides of a triangle. Determine what kind of a triangle we have
# could be: equilateral, isosceles, scalene, right triangle, acute triangle, obtuse triangle.
#calculate area

import math

def triangleApproval(a,b,c):
    if (a+b)<c:
        return False

    elif (b+c)<c:
        return False

    elif (c+a)<b:
        return False

    else:
        print("A triangle is possible to be formed.")
        return True

def detType(a,b,c):
    if a==b==c:
        return 'Equilateral'

    if a==b or a==c or b==c:
        return 'Isosceles'

    else:
        return 'Scalene'

def detAngleType(a,b,c):
    a = a * a
    b = b * b
    c = c * c

    if a >= b or a >= c:
        max = a
        min1 = b
        min2 = c

    elif b>=a or b>=c:
        max = b
        min1 = a
        min2 = c

    else:
        max = c
        min1 = a
        min2 = b

    if min1+min2>max:
        return 'Acute'

    elif min1+min2==max:
        return 'Right Angle'

    else:
        return 'Obtuse'

def area(a,b,c):
    s = (a+b+c)/2 #Calculate "s" (half of the triangles perimeter)
    a = math.sqrt(s*(s-a)*(s-b)*(s-c)) #area formula
    return a

try:
    a = int(input('Enter side A: '))
    b = int(input('Enter side B: '))
    c = int(input('Enter side C: '))

    if triangleApproval(a, b, c) == True:
        print('Triangle type: ' + detType(a, b, c))
        print('Angle type: ' + detAngleType(a, b, c))
        print('Area: ', area(a,b,c))

    else:
        print('Not possible.')

except ValueError:
    print('You did not enter valid integers.')