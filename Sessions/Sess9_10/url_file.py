from urllib.request import urlopen
fd = urlopen("https://en.wikipedia.org/wiki/Main_Page")
for line in fd:
    print(line.decode())