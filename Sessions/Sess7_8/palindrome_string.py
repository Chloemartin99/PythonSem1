#check if a string is a palindrome
s = "Yo, banana boy!"

punctuation = ",.':;!? "
for p in punctuation:
    s = s.replace(p, "")

s = s.lower()
reverse = s[::-1]

if s==reverse:
    print("It is a palindrome")