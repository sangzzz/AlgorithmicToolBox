
# Uses python3
import sys
import random
import math


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        # print(current)
        previous, current = current, previous + current

    return current % 10


def find():
    previous = 0
    current = 1

    tlist = [(0, 1)]
    dlist = [0, 1]
    i = 1
    while True:
        i = i + 1
        previous, current = current, (previous + current) % 10
        if (previous, current) not in tlist:
            tlist.append((previous, current))

        else:
            return i, dlist
        dlist.append(current)


def get_fibonacci_last_digit_fast(n):
    x, digits = find()
    index = n % (x-1)
    return digits[index]


def stress_test():
    while True:
        n = math.floor(random.random() * 10000)
        if get_fibonacci_last_digit_fast(n) != get_fibonacci_last_digit_naive(n):
            print(n, get_fibonacci_last_digit_naive(
                n), get_fibonacci_last_digit_fast(n))
            break
        else:
            print("Success")


if __name__ == '__main__':
    # stress_test()
    n = int(input())
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))
