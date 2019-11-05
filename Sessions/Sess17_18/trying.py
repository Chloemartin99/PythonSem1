listx = [1, 2, 3, 4, 5]

for i in range(5):
    j = i+1

    if j<5:
        print(listx[j], '-', listx[i])

        if listx[j]-listx[i]==1:
            print('yes')

        else:
            print("no")