#multiplication table 1-10 without duplicates
for i in range (1, 11):
    for j in range (i, 11):
        print(str(i)+"x"+str(j)+"="+str((i*j)))
        #alternative way of printing: print(i, "x", "g", "=", i*j)
        #laternative way: print("%d*%d=%d"%(i, j, i*j))

        #alternative way (by jose)- use format function:
        # day = "tuesday"
        #print(" Hello {}. Today is {}".format("Chloe", day))

