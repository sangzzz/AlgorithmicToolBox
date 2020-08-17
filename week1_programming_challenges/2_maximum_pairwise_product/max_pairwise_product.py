# python3

import math
import random


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    i = 0
    big = -1
    max_index1, max_index2 = [-1, -1]
    while i < n:
        if numbers[i] > big:
            max_index1 = i
            big = numbers[i]
        i = i+1
    i = 0
    big = -1
    while i < n:
        if i != max_index1 and numbers[i] > big:
            max_index2 = i
            big = numbers[i]
        i = i+1
    return numbers[max_index1] * numbers[max_index2]


def stress_test():
    n = math.floor(random.random() * 20) + 2
    numbers = []
    for i in range(0, n):
        numbers.append(math.floor(random.random() * 100000))
    product1 = max_pairwise_product(numbers)
    product2 = max_pairwise_product_fast(numbers)
    if product1 != product2:
        print(numbers)
        print(str(product1) + ', ' + str(product2))
        return False
    else:
        print("Success!")
        return True


if __name__ == '__main__':
    # while True:
    #     if stress_test() != True:
    #         break
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(max_pairwise_product_fast(input_numbers))
