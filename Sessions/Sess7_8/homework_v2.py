s = "azzzbjpqrsba"
current = ""
longest = ""

for character in s:
    if current == "":
        current = character
        continue

    if character<current[-1]:
        if len(current)>len(longest):
            longest = current

        current = ""

    current+=character

print(longest)