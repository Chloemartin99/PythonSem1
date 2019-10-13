# generate 100 numbers, print only the prime ones

import random

for i in range(100):
    num = random.randint(0, 1000)
    for j in range (2, num//2):
        if num%j ==0:
            break
        if j == (num // 2) - 1:
            print(num)