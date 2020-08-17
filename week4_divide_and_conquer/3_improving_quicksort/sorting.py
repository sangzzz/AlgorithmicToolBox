# Uses python3
import sys
import random
import math


def partition3(a, l, r):
    # write your code here
    x = a[l]
    j = l
    for i in range(l+1, r+1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    k = j
    for i in range(j + 1, r + 1):
        if a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[j], a[k] = a[k], a[j]
    return j, k


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    # m = partition2(a, l, r)
    j, k = partition3(a, l, r)
    randomized_quick_sort3(a, l, j - 1)
    randomized_quick_sort3(a, k + 1, r)


def randomized_quick_sort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition2(a, l, r)
    # j, k = partition3(a, l, r)
    randomized_quick_sort2(a, l, m - 1)
    randomized_quick_sort2(a, m + 1, r)


def stress_test():
    while True:
        n = math.floor(random.random() * 500) + 1
        a = []
        for i in range(0, n):
            a.append(math.floor(random.random() * 10))
        b = [i for i in a]
        randomized_quick_sort2(a, 0, n-1)
        # print(a)
        # print(b)
        randomized_quick_sort3(b, 0, n-1)
        if a == b:
            print("Success")
        else:
            print(a)
            print(b)
            break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # stress_test()
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
