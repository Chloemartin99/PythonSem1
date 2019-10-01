s = "chloes"
store = [""]
counter = 0
temp = ""

for i in s:
    for j in s[1:]:
        if j<i:
            counter=counter+1
        temp = store[counter]+s[s.index(j)-1]
        store.insert(counter, temp)

print(store)