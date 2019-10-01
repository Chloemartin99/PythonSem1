s = "azcbobobegghakl"
current = ""
longest = ""
store=[]

for i in s:
    if current=="":
        current = i

    if i< current[-1]:
        if len(current) > len(longest):
            store.append(current)
            longest = current

        current = i

    else:
        current = current+i


print(longest)
print(store)