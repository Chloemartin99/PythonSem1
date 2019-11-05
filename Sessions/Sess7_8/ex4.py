fd = open("Competition.txt","r")

vowels = "aeiou"
alphabet = " abcdefghijklmnopqrstuvwxyz"
lines = 1
message = ""

for line in fd:
    vowelcount = 0

    for letter in line:
        if letter in vowels:
            vowelcount +=1

    print("Line ", lines, ": ", vowelcount, " vowels.")
    lines+=1
    message+= alphabet[vowelcount]

print(message)


