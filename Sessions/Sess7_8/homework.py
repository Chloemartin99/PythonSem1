s = "azcbobobegghakl"
current = ""
longest = ""

for i in s:
    if current=="":
        current = i

    if i< current[-1]:
        if len(current) > len(longest):
            if s[0]==current[0]:
                current = current[1:]

            longest = current

        current = i

    else:
        current = current+i


print(longest)