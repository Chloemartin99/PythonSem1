# determine the N-th number in the fibonacci series (0,1,1,2,3,5,8,) Fn = Fn-1 + Fn-2

import sys
sys.setrecursionlimit(10000)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print("fibo(5)=", fibo(5))