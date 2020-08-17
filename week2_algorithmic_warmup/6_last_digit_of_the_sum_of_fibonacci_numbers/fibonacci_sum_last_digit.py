# Uses python3
import sys
import math
import random


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def find(m):
    previous = 0
    current = 1
    previousSum = 0
    currentSum = 1
    tlist = [(previousSum, currentSum)]
    dlist = [0, 1]
    i = 1
    while True:
        i = i+1
        previous, current = current, previous+current
        previousSum, currentSum = currentSum, (currentSum+current) % m
        if (previousSum, currentSum) not in tlist:
            tlist.append((previousSum, currentSum))
            dlist.append(currentSum % m)
        else:
            return dlist, i


def fibonacci_sum_fast(n):
    if n <= 1:
        return n
    digits, i = find(10)
    index = n % (i-1)
    # print(find(10))
    return digits[index]


def stress_test():
    while True:
        n = math.floor(random.random()*100000)
        if fibonacci_sum_fast(n) == fibonacci_sum_naive(n):
            print("Success")
        else:
            print(n, fibonacci_sum_fast(n), fibonacci_sum_naive(n))
            break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # stress_test()
    n = int(input())
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))
