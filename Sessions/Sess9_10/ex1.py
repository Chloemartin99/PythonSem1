#Write a function that computes the sum of 10 random numbers
import random
addition = 0

for i in range(10):
    num = random.randint(0,100)
    addition+=num

print(addition)