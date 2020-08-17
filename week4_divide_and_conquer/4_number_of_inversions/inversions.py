# Uses python3
import sys
import math
import random


# def get_number_of_inversions(a, b, left, right):
#     num = 0
#     # write your code here
#     if right == left+1:
#         return num
#     mid = (left + right + 1)//2
#     # print(num)
#     if (mid - left)
#     num += get_number_of_inversions(a, b, left, mid)
#     # print(num)
#     num += get_number_of_inversions(a, b, mid, right)
#     num += merge(a, b, left, mid, right)
#     return num


# def merge(a, b, left, mid, right):
#     i = left
#     j = mid
#     k = left
#     num = 0
#     while i < mid and j < right:
#         print(num)
#         if a[i] <= a[j]:
#             b[k] = a[i]
#             i += 1
#             k += 1
#         else:
#             b[k] = a[j]
#             j += 1
#             k += 1
#             num += (mid - i)
#             # print(num)
#     return num
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    num = 0
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            num += (n1 - i)
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return num


def mergeSort(arr, l, r):
    num = 0
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l+(r-1))//2

        # Sort first and second halves
        num += mergeSort(arr, l, m)
        num += mergeSort(arr, m+1, r)
        num += merge(arr, l, m, r)
    return num


def inversions_naive(a):
    b = len(a)
    count = 0
    for i in range(0, b):
        for j in range(i+1, b):
            if a[i] > a[j]:
                count += 1
    return count


def stress_test():
    while True:
        n = math.floor(random.random()*1000)+1
        a = []
        # b = [0] * n
        for i in range(0, n):
            a.append(math.floor(random.random()*1000))
        i1 = inversions_naive(a)
        i2 = mergeSort(a, 0, n-1)
        if i1 == i2:
            print("Success")
        else:
            print(i1, i2)
            print(n, a)
            break


if __name__ == '__main__':
    # stress_test()
    n = int(input())
    a = list(map(int, input().split()))
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # b = n * [0]
    # print(inversions_naive(a))
    print(mergeSort(a, 0, len(a)-1))
