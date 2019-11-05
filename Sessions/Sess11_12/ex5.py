# determine the N-th number in the fibonacci series (0,1,1,2,3,5,8,) Fn = Fn-1 + Fn-2

n = 2

def fibonacci(n):
    before = 1
    pre_before = 0
    fib = before + pre_before

    if n ==0:
        return pre_before

    elif n==1:
        return before

    for i in range(2,n):
        fib = before + pre_before
        pre_before = before
        before = fib

    return fib

print(fibonacci(n))