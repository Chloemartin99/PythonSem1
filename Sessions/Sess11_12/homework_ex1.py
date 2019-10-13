#Determine the maximum number out of N given numbers, where N is a number typed by the user

nonvalid = 'You did not enter a valid number.'

while True: #in order to give the user a second chance in case of entering a non-number value
    try:
        N = int(input("How many numbers would you like to compare? "))

        if (N<=1):
            print('Program exit.') #Because it means that user does not want to compare any numbers.
            break

        counter = 0
        while counter<N:
            num = int(input('Enter number ' +str(counter+1)+": "))
            if counter==0:
                max = num

            if num>max:
                max = num
            counter += 1

        print("Maximum number: ", max)
        break
    except ValueError:
        print(nonvalid)