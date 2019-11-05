def f2(a, b):
    if b ==0:
        return 1

    print(a, '*', f2(a, b-1))
    return a*f2(a, b-1)

print(f2(2,3))

