#Given 3 numbers, determine what kind of triangle you can form with them

def triangle (a,b,c):
    if a>= b and a >=c:
        max = a
        min1 = b
        min2 = c
    elif b>=a and b>=c:
        max = b
        min1 = a
        min2 = c
    else:
        max = c
        min1 = a
        min2 = b
    if min1+min2>max:
        print ("We can make a triangle")
    else:
        print("We can't make a triangle")
        return
    if min1==min2==max:
        print("Equilateral")
    elif min1== min2 or min2==max or min1==max:
        print("Isosceles")
    else:
        print("Scalene")
    if max*max== min1*min1+min2*min2:
        print("Right Angle")
    elif max*max> min1*min1+min2*min2:
        print("Obtuse")
    else:
        print("Acute")


triangle(5,4,5)