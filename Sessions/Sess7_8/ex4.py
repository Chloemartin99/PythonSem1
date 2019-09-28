file = open("Competition.txt","r")
print (file)

vowels = "aeiou"
alphabet = " abcdefghijklmnopqrstuvwxyz"
numbervowels = 0

for line in file:
    if vowels in line in file:
        numbervowels = numbervowels + 1

    print(alphabet[numbervowels])

