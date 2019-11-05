#Given 3 numbers, determine what kind of triangle you can form with them
a=5
b=4
c=5

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

if triangleApproval(a,b,c)==True:
    print('Triangle type: '+detType(a,b,c))
    print('Angle type: '+detAngleType(a,b,c))

else:
    print('Not possible.')