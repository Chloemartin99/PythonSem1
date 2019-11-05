#count amount of times the word 'the' appears in an url
from urllib.request import urlopen
fd = urlopen("https://en.wikipedia.org/wiki/Main_Page")

counter = 0
punctuation = '.,<>-=!\/"?!:;[]{}()|_+$#@^%&*'
text = ""

for line in fd:
    text = text+ line.decode().rstrip()

    for p in punctuation:
        text = text.replace(p, " ")
    words = text.split()
print(words)

for word in words:
    if word =='The' or word=='the':
        counter+=1

print(counter)
fd.close()