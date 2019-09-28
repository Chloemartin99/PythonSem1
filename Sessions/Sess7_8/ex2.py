#HarryPotter example
text = "mystring!lol"
punctuation = ",.!;:"
for p in punctuation:
    text = text.replace(p, " ")

words = text.split(" ")
print(words)
