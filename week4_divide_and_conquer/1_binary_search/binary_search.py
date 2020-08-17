# Uses python3
import sys
import random
import math


def binary_search(a, x):
    left, right = 0, len(a)-1
    # if right == 0:
    #     return -1
    # # write your code here
    # mid = (right + left) // 2
    # if a[mid] == x:
    #     return mid
    # elif a[mid] > x:
    #     return mid - binary_search(a[left:mid], x)
    # else:
    #     # if mid+1
    #     return mid + binary_search(a[mid+1:], x)
    while left <= right:
        mid = (left+right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def stress_test():
    n = math.floor(random.random()*1000000 + 2)
    arr = [math.floor(random.random()*100000 - 50000)]*n
    arr.sort()
    linear = []
    binary = []
    test = n//2
    testcase = [math.floor(random.random()*100 - 50)]*test
    for i in testcase:
        if linear_search(arr, i) == binary_search(arr, i):
            print("Success")
        else:
            print("Error")
            print(arr)
            print(testcase)
            print(i)
            break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = (input())
    # m = data[n + 1]
    # a = data[1 : n + 1]
    # stress_test()
    a = list(map(int, input().split()))
    n1 = a[0]
    a = a[1:]
    search = list(map(int, input().split()))
    # for x in search[1:]:
    #     # replace with the call to binary_search when implemented
    #     print(linear_search(a, x), end=' ')
    # print('')
    for x in search[1:]:
        print(binary_search(a, x), end=' ')
