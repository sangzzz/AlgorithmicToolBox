# Uses python3

import sys


def max_dot_product(a, b):
    # write your code here
    res = 0
    a.sort()    # O(nlogn)
    b.sort()    # O(nlogn)
    for i in range(len(a)):
        res += a[i] * b[i]  # O(n)
    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a, b))    # O(nlogn)
