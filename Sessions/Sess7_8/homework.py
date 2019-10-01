s = "azcbobobegghakl"
current = ""
longest = ""
length = len(current)

for i in s:
    if current=="":
        current = i

    if i<=current[-1]:
        if len(current) > len(longest):
            longest = current

        else:
            current = ""

    else:
        current = current+i

print(longest)