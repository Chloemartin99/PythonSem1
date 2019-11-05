fd = open("textfile", "a")

while True:
    answer = input("Do you want to write something? yes or no--> ")
    if answer == 'no':
        break

    text = input("Type in text... ")
    fd.write(text)
    fd.write("\n")

fd.close()

fd = open("textfile", "r")

file = fd.read()
print("This is what your file looks like: "+"\n"+file)