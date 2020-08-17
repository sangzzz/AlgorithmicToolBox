# Uses python3
import sys
import random
import math


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    # A = max(a, b)
    # B = min(a, b)
    # print(A, B)
    if b == 0:
        return a
    else:
        return gcd_fast(b, (a % b))


def stress_test():
    while True:
        a = math.floor(random.random() * 10000)
        b = math.floor(random.random() * 10000)
        if gcd_naive(a, b) == gcd_fast(max(a, b), min(a, b)):
            print("Success")
        else:
            print(a, b)
            break


if __name__ == "__main__":
    # input = sys.stdin.read()
    # stress_test()
    a, b = map(int, input().split())
    # print(gcd_naive(a, b))
    print(gcd_fast(max(a, b), min(a, b)))
