grossprofit = input("Enter your gross profit: ")
children = input("Enter your number of children: ")

try:
    grossprofit = int(grossprofit)
    children = int(children)

    if children>10:
        children = 10

except ValueError:
    print("You did not enter valid numbers")

percentage = 0;
if grossprofit <1000:
    percentage = 10 - children

elif grossprofit <2000:
    percentage = 12 - children

elif grossprofit <4000:
    percentage = 14 - (children*0.5)

else:
    percentage = 18 - (children*0.5)

netprofit = grossprofit - ((grossprofit * percentage)/100)

print("The net profit is: "+str(netprofit)+ "$")
