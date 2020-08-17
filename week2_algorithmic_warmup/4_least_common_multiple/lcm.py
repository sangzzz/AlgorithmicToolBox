# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(a, b):
    # A = max(a, b)
    # B = min(a, b)
    # print(A, B)
    if b == 0:
        return a
    else:
        return gcd_fast(b, (a % b))


def lcm_fast(a, b):
    return a * b // gcd_fast(max(a, b), min(a, b))


if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a, b))
