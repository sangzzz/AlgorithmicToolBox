# Uses python3
import sys
import math
import random


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def find(m):
    previous = 0
    current = 1
    sum = 1
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


def fibonacci_partial_sum_fast(n, m):

    digits, i = find(10)
    index1 = (n-1) % (i-1)
    index2 = (m) % (i-1)
    # print(digits)
    # print(find(10))
    # print(digits[index1], digits[index2])
    if n == 0 or n == 1:
        return digits[index2]
    return abs(10 + digits[index2] - digits[index1]) % 10


def stress_test():
    while True:
        n = math.floor(random.random()*10000)
        m = math.floor(random.random()*10000)
        if fibonacci_partial_sum_fast(min(n, m), max(n, m)) == fibonacci_partial_sum_naive(min(n, m), max(n, m)):
            print("Success")
        else:
            print(min(n, m), max(n, m), fibonacci_partial_sum_fast(
                min(n, m), max(n, m)), fibonacci_partial_sum_naive(min(n, m), max(n, m)))
            break


if __name__ == '__main__':
    # input = sys.stdin.read();
    # stress_test()
    from_, to = map(int, input().split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))
