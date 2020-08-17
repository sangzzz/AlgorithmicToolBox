# Uses python3
import sys
import math
import random


def get_majority_element(a, left, right):
    if left == right:
        return None
    if left + 1 == right:
        return a[left]
    # write your code here
    c1 = get_majority_element(a, left, (left+right-1)//2)
    c2 = get_majority_element(a, (left+right+1)//2, right)
    if c1 == None and c2 == None:
        return None
    elif c1 == None and c2 != None:
        return c2
    elif c2 == None and c1 != None:
        return c1
    elif c1 != c2:
        f1 = freq(a, c1)
        f2 = freq(a, c2)
        if f1 > len(a)//2:
            return c1
        elif f2 > len(a)//2:
            return c2
        else:
            return None
    else:
        return c1


def freq(a, x):
    count = 0
    for i in a:
        if i == x:
            count += 1
    return count
# def get_majority_element(a):
#     # if left == right:
#     #     return -1
#     # if left + 1 == right:
#     #     return a[left]
#     #write your code here
#     num = a
#     while len(num)>0:
#         i = 0
#         x = []
#         while i < len(num):
#             if i == len(num)-1:
#                 x.append()
#             if num[i] == num[i+1]:
#                 x.append(num[i])
#             i = i + 2
#         num = x

#     return -1


def majority_naive(a):
    for i in a:
        if freq(a, i) > (len(a)//2):
            return 1
    return 0


def majority_n(a):
    i = 0
    num = a
    while len(num) > 2:
        x = a[i]
        j = i+1
        while a[j] == x and j < len(a):
            j += 1
        if j != len(a):
            num.remove(x)
            num.remove(a[j])
        else:
            break
    # if len(num)>2:


def stress_test():
    while True:
        n = math.floor(random.random()*10+2)
        a = [math.floor(random.random()*3)+1] * n
        m1 = majority_naive(a)
        m2 = get_majority_element(a, 0, n-1)
        if (m1 == 1 and m2 != None) or (m1 == 0 and m2 == None):
            print("Success!")
        else:
            print(a)
            break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # stress_test()
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(1)
        sys.exit()
    elif n == 2:
        if a[0] == a[1]:
            print(1)
        else:
            print(0)
        sys.exit()
    a.sort()
    if freq(a, a[n//2]) > n//2:
        print(1)
    else:
        print(0)
    # if get_majority_element(a, 0, n-1) != None:
    #     print(1)
    # else:
    #     print(0)
