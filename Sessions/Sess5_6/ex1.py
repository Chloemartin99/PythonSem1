base = input("Enter number a: ")
power = input("Enter number b: ")

try:
    base = int(base)
    power = int(power)

except ValueError:
    print("You did not enter numbers in a valid format.")

to_add = 1
for i in range(power):
    sum = 0

    for j in range(base):
        sum = sum + to_add

    to_add = sum

print(to_add)