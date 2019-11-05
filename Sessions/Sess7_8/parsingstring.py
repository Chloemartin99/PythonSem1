s = "http://google.com and then there could be http://yahoo.com or even a website like http://bbc.co.uk"
start = 0

while True:

    start = s.find("http://", start)
    if start == -1:
        break

    end = s.find(" ",start)
    if end == -1:
        print(s[start:])
        break

    print(s[start:end])
    start = end