#10 + common words in a file
punctuation2 = ',.:!?"()[]{}-*<>'
def common_words(file):
    fd = open('Potter', "r")
    d = {}
    for line in fd:
        for c in punctuation2:
            line = line.replace(c, " ")
        words = line.split()

        for words in words:
            if words in d:
                d[words] += 1

            else:
                d[words]=1

    values = list(d.values())
    values.sort(reverse = True)
    common = []

    for numbers in values[:10]:
        for keys in d:
            if d[keys] == numbers:
                common.append((keys, numbers))

    print("the most common words are: ")
    for i in common:
        print(i[0], i[1], " times")

file = 'Potter'
common_words(file)