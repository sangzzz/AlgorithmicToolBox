# Uses python3
from sys import stdin
import math
import random


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def find(m):
    previous = 0
    current = 1
    previousSum = 0
    currentSum = 1
    tlist = [(0, 1)]
    dlist = [0, 1]
    i = 1
    while True:
        i = i + 1
        previous, current = current, (previous + current)
        previousSum, currentSum = currentSum, (
            currentSum + (current*current)) % m
        if (previousSum, currentSum) != (0, 1):
            tlist.append((previousSum, currentSum))
            dlist.append(currentSum % m)
        else:
            return i, dlist


def get_fibonacci_last_digit_fast(n):
    x, digits = find(10)
    # print(find(10))
    index = n % (x-1)
    return digits[index]


def stress_test():
    while True:
        n = math.floor(random.random() * 10000)
        if get_fibonacci_last_digit_fast(n) != fibonacci_sum_squares_naive(n):
            print(n, fibonacci_sum_squares_naive(n),
                  get_fibonacci_last_digit_fast(n))
            break
        else:
            print("Success")


if __name__ == '__main__':
    # stress_test()
    n = int(input())
    # print(fibonacci_sum_squares_naive(n))
    print(get_fibonacci_last_digit_fast(n))
