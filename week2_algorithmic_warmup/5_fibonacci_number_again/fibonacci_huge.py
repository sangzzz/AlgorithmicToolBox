# Uses python3
import sys
import math
import random


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def find(n, m):
    previous = 0
    current = 1

    tlist = [(0, 1)]
    dlist = [0, 1]
    i = 1
    while True:
        i = i + 1
        previous, current = current, (previous + current) % m
        if (previous, current) not in tlist:
            tlist.append((previous, current))

        else:
            return i, dlist
        dlist.append(current)


def get_fibonacci_huge_fast(n, m):
    if m == 1:
        return 0
    x, digits = find(n, m)
    index = n % (x-1)
    return digits[index]


def stress_test():
    while True:
        m = math.floor(random.random() * 10000) + 1
        n = math.floor(random.random() * 10000)
        if get_fibonacci_huge_fast(n, m) == get_fibonacci_huge_naive(n, m):
            print("Success")
        else:
            print(n, m)
            break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # stress_test()
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))
