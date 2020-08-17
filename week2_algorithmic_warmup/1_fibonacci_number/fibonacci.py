import random
# Uses python3


def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    a = 0
    b = 1
    i = 2
    if n <= 1:
        return n
    while i <= n:
        c = a+b
        a = b
        b = c
        i = i+1
    return c


def stress_test():
    for i in range(0, 31):
        if calc_fib(i) != calc_fib_fast(i):
            print(i)
            return False
    return True


# if stress_test():
#     print("Success")
# else:
#     print("Failure")
n = int(input())
# print(calc_fib(n))
print(calc_fib_fast(n))
