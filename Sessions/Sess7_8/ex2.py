fd = open("Potter", "r")
#incomplete
punctuation = ",.:!?()[]{}-*<>’‘'"
lines = []
for line in fd:
    for p in punctuation:
        line = line.replace(p, " ")

    lines = lines+line.split()

print(lines)